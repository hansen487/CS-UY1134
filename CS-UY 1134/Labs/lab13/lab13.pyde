maxlat=40.6903
minlat=40.7061
maxlon=-73.9728
minlon=-74.0065

class Graph:

  #------------------------- nested Vertex class -------------------------
  class Vertex:
    """Lightweight vertex structure for a graph."""
    __slots__ = '_element'
  
    def __init__(self, x):
      """Do not call constructor directly. Use Graph's insert_vertex(x)."""
      self._element = x
  
    def element(self):
      """Return element associated with this vertex."""
      return self._element
  
    def __hash__(self):         # will allow vertex to be a map/set key
      return hash(id(self))

    def __str__(self):
      return str(self._element)
    
  #------------------------- nested Edge class -------------------------
  class Edge:
    """Lightweight edge structure for a graph."""
    __slots__ = '_origin', '_destination', '_element'
  
    def __init__(self, u, v, x):
      """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
      self._origin = u
      self._destination = v
      self._element = x
  
    def endpoints(self):
      """Return (u,v) tuple for vertices u and v."""
      return (self._origin, self._destination)
  
    def opposite(self, v):
      """Return the vertex that is opposite v on this edge."""
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      return self._destination if v is self._origin else self._origin
      raise ValueError('v not incident to edge')
  
    def element(self):
      """Return element associated with this edge."""
      return self._element
  
    def __hash__(self):         # will allow edge to be a map/set key
      return hash( (self._origin, self._destination) )

    def __str__(self):
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)
    
  #------------------------- Graph methods -------------------------
  def __init__(self, directed=False):
    """Create an empty graph (undirected, by default).

    Graph is directed if optional paramter is set to True.
    """
    self._outgoing = {}
    # only create second map for directed graph; use alias for undirected
    self._incoming = {} if directed else self._outgoing

  def _validate_vertex(self, v):
    """Verify that v is a Vertex of this graph."""
    if not isinstance(v, self.Vertex):
      raise TypeError('Vertex expected')
    if v not in self._outgoing:
      raise ValueError('Vertex does not belong to this graph.')
    
  def is_directed(self):
    """Return True if this is a directed graph; False if undirected.

    Property is based on the original declaration of the graph, not its contents.
    """
    return self._incoming is not self._outgoing # directed if maps are distinct

  def vertex_count(self):
    """Return the number of vertices in the graph."""
    return len(self._outgoing)

  def vertices(self):
    """Return an iteration of all vertices of the graph."""
    return self._outgoing.keys()

  def edge_count(self):
    """Return the number of edges in the graph."""
    total = sum(len(self._outgoing[v]) for v in self._outgoing)
    # for undirected graphs, make sure not to double-count edges
    return total if self.is_directed() else total // 2

  def edges(self):
    """Return a set of all edges of the graph."""
    result = set()       # avoid double-reporting edges of undirected graph
    for secondary_map in self._outgoing.values():
      result.update(secondary_map.values())    # add edges to resulting set
    return result

  def get_edge(self, u, v):
    """Return the edge from u to v, or None if not adjacent."""
    self._validate_vertex(u)
    self._validate_vertex(v)
    return self._outgoing[u].get(v)        # returns None if v not adjacent

  def degree(self, v, outgoing=True):   
    """Return number of (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to count incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    return len(adj[v])

  def incident_edges(self, v, outgoing=True):   
    """Return all (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to request incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    for edge in adj[v].values():
      yield edge

  def insert_vertex(self, x=None):
    """Insert and return a new Vertex with element x."""
    v = self.Vertex(x)
    self._outgoing[v] = {}
    if self.is_directed():
      self._incoming[v] = {}        # need distinct map for incoming edges
    return v
      
  def insert_edge(self, u, v, x=None):
    if self.get_edge(u,v) is None:
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
    
class Map:
    def __init__(self, vertices, edges):
       self._graph = Graph()
       self._vertices = vertices
       self._edges = edges
       self._dictionary = {}
    def add_vertices(self):
        for i in self._vertices:
            v = self._graph.insert_vertex(i)
            self._dictionary[i] = v
    def add_edges(self):
        for i in self._edges:
            self._graph.insert_edge(self._dictionary[i[0]], self._dictionary[i[1]])
        return self._graph.edges()

       
import copy
import xml.etree.ElementTree as etree
def getMap(file):
    G=open(file)
    root = etree.parse(G).getroot()
    v={}
    for child in root:
        if (child.tag=="node"):
            v[child.attrib["id"]]=(float(child.attrib["lon"]),float(child.attrib["lat"]))
    e=[]
    for child in root:
        if (child.tag=="way"):
            a=[]
            for gc in child:
                if gc.tag=="nd":
                    a.append(v[gc.attrib["ref"]])
            for i in range(len(a)-1):
                e.append((a[i],a[i+1]))
    return list(v.values()),e

V,E = getMap('map.osm')
M = Map(V, E)
M.add_vertices()
edges = M.add_edges()

def mouseToScreen(mx,my):
    return (minlon+(mx/float(width))*(maxlon-minlon), minlat+(my/float(height))*(maxlat-minlat))

def colorchange():
    minimum = 100
    for i in edges:
        x,y = i.endpoints()
        cursor = mouseToScreen(mouseX, mouseY)
        d = dist(cursor[0], cursor[1], y._element[0], y._element[1]) 
        if d < minimum:
            minimum = d
            origin, endpoint = x, y
    return (origin, endpoint)

def BFS(g, s, discovered, x):
  """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.

  discovered is a dictionary mapping each vertex to the edge that was used to
  discover it during the BFS (s should be mapped to None prior to the call).
  Newly discovered vertices will be added to the dictionary as a result.
  """
  level = [s]                        # first level includes only s
  count = 0
  while count < 50:
    next_level = []                  # prepare to gather newly found vertices
    for u in level:
      for e in g.incident_edges(u):  # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:      # v is an unvisited vertex
          discovered[v] = e          # e is the tree edge that discovered v
          a, b = e.endpoints()
          r = 5*count
          blu = 255-5*count
          stroke(r, 0, blu)
          if (x, s) != (a, b):
            line(a._element[0], a._element[1], b._element[0], b._element[1])
          next_level.append(v)       # v will be further considered in next pass
    level = next_level               # relabel 'next' level to become current
    count += 1


def BFS_complete(g):
  """Perform BFS for entire graph and return forest as a dictionary.

  Result maps each vertex v to the edge that was used to discover it.
  (vertices that are roots of a BFS tree are mapped to None).
  """
  forest = {}
  for u in g.vertices():
    if u not in forest:
      forest[u] = None            # u will be a root of a tree
      BFS(g, u, forest)
  return forest
 

def setup():
    background(255)
    size(1500,1500)
    scale(float(width)/(maxlon-minlon),float(height)/(maxlat-minlat))
    translate(-minlon,-minlat)
    strokeWeight(0.00001)
def draw():
    background(255)
    global minlat
    global minlon
    global maxlon
    global maxlat
    scale(float(width)/(maxlon-minlon),float(height)/(maxlat-minlat))
    translate(-minlon,-minlat)
    strokeWeight(0.00001)
    stroke(128,128,128)
    for i in edges:
        x,y = i.endpoints()
        line(x._element[0], x._element[1], y._element[0], y._element[1])
    stroke(0, 255, 0)
    strokeWeight(.0001)
    x, y = colorchange()
    line(x._element[0], x._element[1], y._element[0], y._element[1])
    proximity = {}
    strokeWeight(.00001)
    BFS(M._graph, y, proximity, x)
    # stroke(0,0,255)
    # for v in proximity:
    #     edge = proximity[v]
    #     a, b = edge.endpoints()
    #     if (a, b) != (x, y):
    #         line(a._element[0], a._element[1], b._element[0], b._element[1])
        
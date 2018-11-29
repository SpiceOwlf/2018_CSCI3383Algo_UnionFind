
public interface UnionFind {
	public void union(int x, int y);
	public boolean find(int x, int y);
	public int numberComponents();
	public int[] returnGraph();
	public int getCount();
}

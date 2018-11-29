
public class QuickUnion implements UnionFind{
	private int numberComponents;
	private int[] id; //can later change to ArrayList;
	private int count; //count how many times we try to get to parents
	
	public QuickUnion(int n) {
		this.numberComponents = n;
		this.id = new int[n];
		for (int i = 0; i < n; i++) {
			id[i] = i;
		}
	}
	
	@Override
	public void union(int x, int y) {
		// TODO Auto-generated method stub
		int xParent = findParent(x);
		int yParent = findParent(y);
		
		if (xParent != yParent) {
			numberComponents--;
			id[yParent] = id[xParent];
		}
		
	}

	@Override
	public boolean find(int x, int y) {
		// TODO Auto-generated method stub
		return findParent(x) == findParent(y);
	}

	public int findParent(int x) {
		// TODO Auto-generated method stub
		while (id[x] != x) {
			x = id[x];
			count++;
		}
		return x;
	}

	@Override
	public int numberComponents() {
		// TODO Auto-generated method stub
		return numberComponents;
	}

	@Override
	public int[] returnGraph() {
		// TODO Auto-generated method stub
		return this.id;
	}

	public int getCount() {
		return this.count;
	}

}

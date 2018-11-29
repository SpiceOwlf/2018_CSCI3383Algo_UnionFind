
public class QuickFind implements UnionFind{
	private int numberComponents;
	//each Id's value represents the root of current val;
	private int[] id;
	private int count;
	
	
	public QuickFind(int n) {
		this.numberComponents = n;
		this.id = new int[n];
		for (int i = 0; i < n; i++) {
			id[i] = i;
		}
	}

	//always merge the second one's Parent to the first one's Parent;
	@Override
	public void union(int x, int y) {
		// TODO Auto-generated method stub
		int xParent = id[x];
		int yParent = id[y];
		if (xParent != yParent) {
			numberComponents --;
			for (int i = 0; i < id.length; i++) {
				count++;
				if (id[i] == yParent) {
					id[i] = xParent;
				}
			}
		}
	}

	@Override
	public boolean find(int x, int y) {
		// TODO Auto-generated method stub
		return id[x] == id[y];
	}

	public int findParent(int x) {
		// TODO Auto-generated method stub
		return id[x];
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

	@Override
	public int getCount() {
		// TODO Auto-generated method stub
		return this.count;
	}


}

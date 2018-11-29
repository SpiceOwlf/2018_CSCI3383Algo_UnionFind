import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.time.Duration;
import java.time.Instant;

public class TestUnionFind {
	// public final static String modelName = "QuickFind";
	// public final static String modelName = "QuickUnion";
	// public final static String modelName = "WeightedQuickUnion";
	public final static String modelName = "WeightedCompression";

	public final static int numNodes = 5000;
	public final static int numUnion = 100000;
	public final static String path = "/Users/MedicalDoctor/Desktop/Algorithm_FinalProject/JavaVersion/Percolation/Random_union_case/";
	public final static String inputFilePrefix = Integer.toString(numNodes) + "_" + Integer.toString(numUnion) + "_";
	public final static String outputFilePrefix = Integer.toString(numNodes) + "_" + Integer.toString(numUnion) + "_" + modelName + "_";
	public final static String endFile = ".txt";



//	private static void printArray(int[] arr) {
//		for (int x : arr) {
//			System.out.print(x + " ");
//		}
//	}

	private static void writeToOutput(String output_fileName, long stopTime) {
		File f = new File(output_fileName);
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter(f, true));
            bw.append(stopTime+"\n");
            bw.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
	}

	private static void runTest(int index) {
		BufferedReader reader;
		UnionFind uf = null;
		String inputFileName = path + inputFilePrefix + Integer.toString(index) + endFile;
		String outputFileName = path + outputFilePrefix + Integer.toString(index) + endFile;
		int union_iteration = 0;
		//boolean first = true;

		try {
			reader = new BufferedReader(new FileReader (inputFileName));
			String line = reader.readLine();
			int numNodes = Integer.parseInt(line);
			uf = new WeightedCompressionOneQuickUnion(numNodes);

			//System.out.println(numNodes);

			Instant startTime = Instant.now();
			line = reader.readLine();
			while (line != null) {
				//read the first one which is always the number of nodes
					union_iteration += 1;

					//fetch the number;
					int space_Index = line.indexOf(' ');
					int first_Number = Integer.parseInt(line.substring(0, space_Index));
					int second_Number = Integer.parseInt(line.substring(space_Index + 1));
					uf.union(first_Number, second_Number);

					//check when it becomes a single component
//					if (uf.numberComponents() == 1 && first ) {
//						System.out.println("Becomes 1 at " + union_iteration);
//						first = false;
//					}

					if (union_iteration % 100 == 0) {
							Instant endSubTime = Instant.now();
							Duration subResult = Duration.between(startTime, endSubTime);
							long subStopTime = subResult.toMillis();
							writeToOutput(outputFileName, subStopTime);
							//"The" + union_iteration + "takes" +
							//System.out.println(subStopTime);
					}

					//System.out.println(first_Number + "," + second_Number);
					line = reader.readLine();
			}
			Instant endTime = Instant.now();

			Duration result = Duration.between(startTime, endTime);
	    	long stopTime = result.toMillis();
	    	System.out.println("The time that it takes to union the graph is" + stopTime);
	    	System.out.println("The number of counts" + uf.getCount());
//	    	printArray(uf.returnGraph());

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i = 0; i < 5; i++) {
			runTest(i);
		}

	}

}

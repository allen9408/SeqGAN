package SemiSyntheticDataGenerator;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Get122TracesActivityIndex {

	public static void main(String[] args) throws IOException {
		BufferedReader br = null;
		/* input1: 122tracesOrigin.csv to get activities' index in List a */
		String filePath ="/Users/guoyifeng/Downloads/getSequentialPattern/122tracesOrigin.csv";

		/*
		 * input2: to reverse sequential pattern in number format back to string
		 * format
		 */
		//String filePath2 = "output/test.txt";
//
		/*
		 * input1-2: 122tracesGenerated.csv to get activities' index in List a
		 */
		//String filePath = "/Users/guoyifeng/Downloads/MatlabPlotForModel/PCA/122Generated.csv";
		
		/*
		 * input1-3: 122+122traces_ori_gen.csv to get mixed activities' index in List a
		 */
//		String filePath = "/Users/guoyifeng/Downloads/MatlabPlotForModel/PCA/122+122traces_ori_gen.csv";
		
		/*
		 * input1-4: 122HeuristicGeneratedSequences to get mixed activities' index in List a
		 */
		//String filePath = "/Users/guoyifeng/Downloads/MatlabPlotForModel/PCA_Heuristic/122HeuristicGeneratedSequences.txt";
		
		/*
		 * input1-5: Random122GeneratedTraces to get mixed activities' index in List a
		 */
		//String filePath = "/Users/guoyifeng/Downloads/MatlabPlotForModel/PCA_Random122From5000/Random122GeneratedTraces2.csv";
		
		try {
			br = new BufferedReader(new FileReader(filePath));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		ArrayList<String[]> arr = new ArrayList<>(); // to store input1
		ArrayList<String> arr2 = new ArrayList<>(); // to store input2
		String line = "";
		String[] b;
		String splitBy = ","; // to read input1;
		//String splitBy = "#SUP"; // to read input2
		while ((line = br.readLine()) != null) {
			b = line.split(splitBy);
			arr.add(b); // input1
			//arr2.add(b[0]);// input2
		}
		br.close();

		/**
		 * to check the input1 is stored normally
		 */
//		for (int i = 0; i < arr.size(); i++) {
//			for (int j = 0; j < arr.get(i).length; j++) {
//				System.out.print(arr.get(i)[j] + " ");
//			}
//			System.out.println();
//		}
		
		/**
		 * to check the input2 is stored normally
		 */
//		for (int i = 0; i < arr2.size(); i++) {
//			System.out.println(arr2.get(i));
//		}


		List<String> a = new ArrayList<String>(Arrays.asList("Pt_arrival", "Visual_assessment_AA",
				"Chest_Auscultation_BA", "R_DP_PT_PC", "Total_Verbalized_GCS", "Right_pupil_PU", "Left_pupil_PU",
				"Visual_inspection_H", "Palpation_H", "Palpation_F", "Visual_inspection_F", "L_Visual_inspection_EAR",
				"Visual_inspection_N", "R_Visual_inspection_EAR", "R_otoscopy_EAR", "Visual_inspection_M",
				"Palpation_NE", "Visual_inspection_NE", "L_otoscopy_EAR", "Palpation_C", "Visual_inspection_C",
				"Palpation_A", "Visual_inspection_A", "Stability_PE", "Palpation_RLE", "Visual_inspection_RLE",
				"Palpation_LLE", "Visual_inspection_LLE", "Palpation_LUE", "Visual_inspection_LUE", "Palpation_RUE",
				"Visual_inspection_RUE", "Log_roll_BK", "Rectal_BK", "Pt_departure", "Verbal_assessment_AA",
				"C_spine_BK", "Visual_inspection_G", "Visual_inspection_BK", "T_spine_BK", "L_spine_BK", "L_DP_PT_PC",
				"L_visual_inspection_EY", "R_visual_inspection_EY"));

		/**
		 * to print the activity index in a for input1
		 */
		for (int i = 0; i < arr.size(); i++) {
			for (int j = 0; j < arr.get(i).length; j++) {
				System.out.print(a.indexOf(arr.get(i)[j]) + " -1 ");
			}
			System.out.print(-2);
			System.out.println();
		}

		
		/**
		 * to reverse sequential pattern in number format back to string format
		 */
//		String filePath2 = "output/test.txt";
////
//		try {
//			br = new BufferedReader(new FileReader(filePath2));
//		} catch (FileNotFoundException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
////
//		ArrayList<String[]> arr3 = new ArrayList<>(); // to store input1
//		String line2 = "";
//		String[] b2;
//		String splitBy2 = " ";
//		while ((line2 = br.readLine()) != null) {
//			b2 = line2.split(splitBy2);
//			arr3.add(b2); // input2
//		}
//		br.close();
//		for (int i = 0; i < arr3.size(); i++) {
//			for (int j = 0; j < arr3.get(i).length; j++) {
//				System.out.print(arr3.get(i)[j] + " ");
//			}
//			System.out.println();
//		}
		
//		for (int i = 0; i < arr3.size(); i++) {
//			for (int j = 0; j < arr3.get(i).length; j++) {
//				System.out.print(a.get(Integer.parseInt(arr3.get(i)[j])) + " ");
//			}
//			System.out.println();
//		}
	
		
		//System.out.println(a.get(Integer.parseInt(arr3.get(68)[1])));
	}

}

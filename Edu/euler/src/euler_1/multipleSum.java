package euler_1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/* https://projecteuler.net/problem=1
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, 
 * we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 * Output="Sum of multiples from 1 to 1000 for factors [3, 5] is = 233168"
 * ANSWER=233168
 */
public class multipleSum {

	private static List<List<Integer>> factorMultList = new ArrayList<List<Integer>>();
	private static List<Integer> factorSumList = new ArrayList<Integer>();
	private static int multiSummation = 0;
	private Range range;
	private int[] factor;
	/*
	 * Define Range object to hold lower and upper bound of natural number
	 */
	private static class Range {
		private final int lowerBound;
		private final int upperBound;
		
		public Range(int lowerBound, int upperBound) throws Exception{
			if (lowerBound < 0){
				throw new Exception("lower bound range must be a Natural Number");
			}
			this.lowerBound = lowerBound;
			this.upperBound = upperBound;
		}
		
	}
	
	public multipleSum(int lowerBound, int upperBound, int[] factor){
		
		try {
			this.range = new multipleSum.Range(lowerBound,upperBound);
			this.factor = factor;

		
		} catch (Exception e) {
			e.printStackTrace();
			System.exit(1);
		}
	}
	
	public int calculate(){
		for (int fact:factor){
			factorMultList.add(getMultiples(range,fact));
		}
		for (List<Integer> list:factorMultList){
			for (int mult:list){
				if(!factorSumList.contains(mult)){
					factorSumList.add(mult);
				}
			}
		}
	
		multiSummation = sumMultiples(factorSumList);
		
		System.out.printf("Sum of multiples from %d to %d for factors %s is = %d",range.lowerBound,range.upperBound,Arrays.toString(factor),multiSummation);
		
		return multiSummation;
	}
	
	private static List<Integer> getMultiples(Range range, int factor){
		List<Integer> multiples = new ArrayList<Integer>();
		for(int x = 1; x*factor < range.upperBound && x*factor >= range.lowerBound; x++ ){
			multiples.add(x*factor);
		}
		return multiples;
	}
	
	private static int sumMultiples(List<Integer> multiples){
		int multipleSumResult = 0;
		for (int mult:multiples){
			multipleSumResult+=mult;
		}
		return multipleSumResult;
		
	}
}

package euler_1;

public class main {
	public static void main(String[] args){
		int[] factor = {3,5};
		int result = new multipleSum(0, 1000, factor).calculate();
		System.out.println("\n"+result);

	}
}

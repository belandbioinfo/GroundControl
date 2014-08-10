package euler_2;

import java.util.LinkedList;
import java.util.List;

public class getEven {
	
	private List<Integer> list;
	private List<Integer> sendList = new LinkedList<Integer>();
	
	public getEven(LinkedList<Integer> list){
		this.list = list;
	}
	
	public List<Integer> returnEven(){
		for (int item:this.list){
			if (item % 2 == 0){
				this.sendList.add(item);
			}
		}
		
		return sendList;
	}
	
}

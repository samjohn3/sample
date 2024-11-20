public class Bubble {
    public static void main(String[] args) {
        //sort -->3 2 4 1 -->1 2 3 4
        int[] arr = {3, 2, 4, -1,2,3,53,346,1,451};   //index value 0 1 2 3
        // bubble sort
        for (int i = 0; i < arr.length-1; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] > arr[j]) {
                    int temp = arr[i];  //i value in temp location
                    arr[i] = arr[j]; //i value move to j
                    arr[j] = temp;      //j place move to temp
                }
            }
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
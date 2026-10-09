class Solution {
    public int[] replaceElements(int[] arr) {
        int n=arr.length;
        int max=arr[n-1];
          for(int i=n-1;i>=1;i--){
            if(max>arr[i-1]){
                arr[i-1]=max;
            }else if(arr[i]<arr[i-1]){
                int temp=arr[i-1];
                arr[i-1]=max;
                max=temp;
            }
            }   
            arr[n-1]=-1;
            return arr;   
    }
}
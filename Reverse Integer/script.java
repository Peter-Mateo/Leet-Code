public class script {
    public static void main(String[] args){
        class Solution{
            public int reverse(int x){
                if (x == 0){
                    return 0;
                }
                String numbers = Integer.toString(x);
                String last = "";
                char neg = '-';
                if (numbers.contains("-")){
                    last += "-";
                }
                for(int i = numbers.length() - 1; i >= 0; i--){
                    if(numbers.charAt(i) == neg){
                        continue;
                    }
                    last += numbers.charAt(i);
                }
                if(last.indexOf("0") == 0){
                    String newLast = last.substring(1);
                    System.out.println(newLast);
                    return Integer.parseInt(newLast);
                }
                try {
                    int ehh = Integer.parseInt(last);
                    return ehh;
                } catch(NumberFormatException e) {
                    return 0;
                }
            }
        }
        Solution sol = new Solution();
        sol.reverse(1534236469);
    }
}

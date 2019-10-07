/*
 * @lc app=leetcode.cn id=6 lang=java
 *
 * [6] Z 字形变换
 *
 * https://leetcode-cn.com/problems/zigzag-conversion/description/
 *
 * algorithms
 * Medium (45.05%)
 * Likes:    419
 * Dislikes: 0
 * Total Accepted:    62.1K
 * Total Submissions: 137.7K
 * Testcase Example:  '"PAYPALISHIRING"\n3'
 *
 * 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
 * 
 * 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
 * 
 * L   C   I   R
 * E T O E S I I G
 * E   D   H   N
 * 
 * 
 * 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
 * 
 * 请你实现这个将字符串进行指定行数变换的函数：
 * 
 * string convert(string s, int numRows);
 * 
 * 示例 1:
 * 
 * 输入: s = "LEETCODEISHIRING", numRows = 3
 * 输出: "LCIRETOESIIGEDHN"
 * 
 * 
 * 示例 2:
 * 
 * 输入: s = "LEETCODEISHIRING", numRows = 4
 * 输出: "LDREOEIIECIHNTSG"
 * 解释:
 * 
 * L     D     R
 * E   O E   I I
 * E C   I H   N
 * T     S     G
 * 
 * 
 */

// @lc code=start
class Solution {
    public String convert(String s, int numRows) {
        if (numRows<=1) {
            return s;
        }
        if (s.length()<=numRows) {
            return s;
        }
        char[][] matrix = new char[numRows][s.length()*(numRows-1)/((numRows-1)*2)+1];
        int i = 0;
        int j = 0;
        
        boolean flag = true;
        for (int k = 0; k < s.length(); k++) {
            char c = s.charAt(k);

            flag = flag ^ (k > 0 && (i == 0 || i == numRows - 1));

            if (flag) {
                matrix[i][j] = c;
                i++;
            } else {
                matrix[i][j] = c;
                i--;
                j++;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int m = 0; m < matrix.length; m++) {
            for (int n = 0; n < matrix[0].length; n++) {
                if (matrix[m][n] != '\u0000') {
                    sb.append(matrix[m][n]);
                }
            }
        }
        return sb.toString();
    }
}
// @lc code=end

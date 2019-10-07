/*
 * @lc app=leetcode.cn id=7 lang=java
 *
 * [7] 整数反转
 *
 * https://leetcode-cn.com/problems/reverse-integer/description/
 *
 * algorithms
 * Easy (33.07%)
 * Likes:    1373
 * Dislikes: 0
 * Total Accepted:    196.5K
 * Total Submissions: 594.1K
 * Testcase Example:  '123'
 *
 * 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
 * 
 * 示例 1:
 * 
 * 输入: 123
 * 输出: 321
 * 
 * 
 * 示例 2:
 * 
 * 输入: -123
 * 输出: -321
 * 
 * 
 * 示例 3:
 * 
 * 输入: 120
 * 输出: 21
 * 
 * 
 * 注意:
 * 
 * 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回
 * 0。
 * 
 */

// @lc code=start
class Solution {
    public int reverse(int x) {
        int a = x % 10;
        int b = x / 10;
        if (x > 0) {
            while (b > 0) {
                if (a > 214748364) {
                    return 0;
                }
                a = a * 10 + b % 10;
                b = b / 10;
            }
            return a;
        } else {
            while (b < 0) {
                if (a < -214748364) {
                    return 0;
                }
                a = a * 10 + b % 10;
                b = b / 10;
            }
            return a;
        }
    }
}
// @lc code=end

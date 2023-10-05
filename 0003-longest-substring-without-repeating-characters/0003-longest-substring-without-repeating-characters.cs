public class Solution {
    public int LengthOfLongestSubstring(string s)
    {
        int len = s.Length;
        
        if (len == 1)
            return len;
        
        int res = 0;
        
        for (int i = 0; i < len; i++)
        {
            char c = s[i];
            string current = "" + c;
            
            for (int j = i + 1; j < len; j++)
            {
                char c2 = s[j];                
                if (current.Contains(c2))
                {
                    res = Math.Max(res, current.Length);
                    break;
                }
                current += c2;
            }
            res = Math.Max(res, current.Length);
        }
        
        return res;
    }
}
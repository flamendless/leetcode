function findMedianSortedArrays(nums1: number[], nums2: number[]): number
{
    let median: number = 0;
    let merged: number[] = nums1.concat(nums2)
        .sort((a: number, b: number) => a - b);
    let pivot: number = Math.floor(merged.length/2);
    
    if (merged.length % 2 == 0)
    {
        pivot = Math.floor(pivot);
        let a: number = merged[pivot - 1];
        let b: number = merged[pivot];
        return (a + b)/2;
    }
    
    return merged[pivot];
};
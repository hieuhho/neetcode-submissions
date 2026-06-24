class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)

        max_len = l1 + l2
        half_len = max_len // 2

        l = 0
        r = l1 - 1

        while True:
            i = (l + r) // 2 # nums1 middle
            j = half_len - i - 2 # num2 left side

            nums1_left = nums1[i] if i >= 0 else float("-infinity")
            nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            nums2_left = nums2[j] if j >= 0 else float("-infinity")
            nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if max_len % 2:
                    return min(nums1_right, nums2_right)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2 
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1
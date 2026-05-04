public class SegmentTree {
    int[] tree;
    int n;

    SegmentTree(int[] arr) {
        n = arr.length;
        if (n == 0) {
            tree = new int[0];
        } else {
            tree = new int[4 * n];
            build(arr, 0, 0, n - 1);
        }
    }

    void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = Math.max(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    int queryMax(int left, int right) {
        if (left < 0 || right >= n || left > right) {
            throw new IllegalArgumentException("Invalid query range");
        }
        return queryMax(0, 0, n - 1, left, right);
    }

    private int queryMax(int node, int start, int end, int left, int right) {
        if (right < start || end < left) {
            return Integer.MIN_VALUE;
        }
        if (left <= start && end <= right) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        int leftMax = queryMax(2 * node + 1, start, mid, left, right);
        int rightMax = queryMax(2 * node + 2, mid + 1, end, left, right);
        return Math.max(leftMax, rightMax);
    }

    void update(int index, int value) {
        if (index < 0 || index >= n) {
            throw new IndexOutOfBoundsException("Index out of bounds: " + index);
        }
        update(0, 0, n - 1, index, value);
    }

    private void update(int node, int start, int end, int index, int value) {
        if (start == end) {
            tree[node] = value;
        } else {
            int mid = (start + end) / 2;
            if (index <= mid) {
                update(2 * node + 1, start, mid, index, value);
            } else {
                update(2 * node + 2, mid + 1, end, index, value);
            }
            tree[node] = Math.max(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    public static void main(String[] args) {
        int[] arr = { 1, 3, 5, 7, 9, 11 };
        SegmentTree segmentTree = new SegmentTree(arr);

        System.out.println("Max in range [1, 4] = " + segmentTree.queryMax(1, 4));
        System.out.println("Max in range [0, 5] = " + segmentTree.queryMax(0, 5));

        segmentTree.update(3, 12);
        System.out.println("After update, max in range [1, 4] = " + segmentTree.queryMax(1, 4));
    }
}
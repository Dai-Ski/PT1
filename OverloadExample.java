class OverloadExample {
    int multiply(int a, int b) {
        return a * b;
    }

    int multiply(int a, int b, int c) {
        return a * b * c;
    }
}

class OverrideParent {
    void show() {
        System.out.println("Parent class method");
    }
}

class OverrideChild extends OverrideParent {
    @Override
    void show() {
        System.out.println("Child class overridden method");
    }

    public static void main(String[] args) {
        // Overloading
        OverloadExample obj = new OverloadExample();
        System.out.println(obj.multiply(2, 3));
        System.out.println(obj.multiply(2, 3, 4));

        // Overriding
        OverrideParent p = new OverrideChild();
        p.show();
    }
}
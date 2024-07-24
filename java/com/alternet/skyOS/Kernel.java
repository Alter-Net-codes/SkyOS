// skyOS 3.0
/*
The next evolution of skyOS, skyOS 3 is a single .class file
that runs in the JVM.
It is pretty useful, and it can also run apps as .class files as well.
*/

package com.alternet.skyOS;

import java.util.Scanner;

Scanner scanner = new Scanner(System.in);

File appClass = null;
URL url = null;
String command = null;
String pwd = System.getProperty("user.dir");
String echo = null;
String appClassPath = null;
URL[] urls = null
ClassLoader classVar = null;
Class<?> cls = null;
String appPackageName = null;

class Kernel {
  public static void print(String text) {
    System.out.println(text);
  }
  public static void main(String[] args) {
    while (True) {
      print("Welcome to skyOS!");
      print("skyOS v3.0");
      print("skyOS> ");
      command = scanner.nextLine();
      if (command == "help") {
        print("help - Show this help list.");
        print("app - Load an app (com.example.test is the package name for the test app).");
        print("echo - Echo some text.")
      }
      else if (command == "app") {
        print("Enter the class file's name> ");
        appClassPath = scanner.nextLine();
        print("Enter the class file's package name> ");
        appPackageName = scanner.nextLine();
        file = new File(pwd + appClassPath + ".class");
        url = file.toURI().toURL();
        urls = new URL[]{url};
        classVar = new URLClassLoader(urls);
        cls = classVar.loadClass(appPackageName);
        Object classMethod = cls.getDeclaredMethod("appMain");
        classMethod.appMain();
        file = null;
        url = null;
        urls = null;
        classVar = null;
        cls = null;
        appClassPath = null;
      else if (command == "echo") {
        print("What to echo> ");
        echo = scanner.nextLine();
        print(echo);
      }
      }
    }
  }
}

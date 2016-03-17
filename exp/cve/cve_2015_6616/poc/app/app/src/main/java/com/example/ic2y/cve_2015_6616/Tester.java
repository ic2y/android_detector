package com.example.ic2y.cve_2015_6616;

import android.util.Log;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

/**
 * Created by ic2y on 15-12-15.
 */
public class Tester {
    static String tag = "2015-CVE-3836";

    public static void write_file(String msg) throws IOException {
        try{
            String path = "/data/local/tmp/done";
            File file = new File(path);
            if(!file.exists()){
                Log.i(tag,"/data/local/tmp/done not exist.");
                file.createNewFile();
            }
            FileOutputStream out = new FileOutputStream(file,false);
            out.write(msg.getBytes());
            out.close();
        }catch (Exception e){
            e.printStackTrace();
        }


    }
    public static void apk_ok(){
        try{
            write_file("apk_ok");
        }catch (IOException e){
            e.printStackTrace();
        }

    }
    public static void apk_done(){
        try{
            write_file("apk_done");
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    public static void apk_crash(){
        try{
            write_file("apk_crash");
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}

package com.example.ic2y.cve_2015_6616;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

import junit.framework.Test;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;

public class testService extends Service implements Runnable{
    String tag = "CVE-2015-6616";

    @Override
    public IBinder onBind(Intent intent) {
        // TODO: Return the communication channel to the service.
        throw new UnsupportedOperationException("Not yet implemented");
    }
    @Override
    public void onCreate(){
        super.onCreate();
        Thread thread=new Thread(this);
        thread.start();
    }

    @Override
    public void run() {
        Log.i(tag,"start test");
        testVul();
        Log.i(tag, "test end");
    }

    public void testVul(){
        try{
            File stagefrightlib = new File("/system/lib/libstagefright.so");
            if(!stagefrightlib.exists() || !stagefrightlib.isFile()){
                Log.i(tag," can not load libstagefright.so");
            }

            ByteArrayOutputStream libStageFrightBAOS = new ByteArrayOutputStream((int)stagefrightlib.length());
            BinaryAssets.copy(new FileInputStream(stagefrightlib), libStageFrightBAOS);
            byte[] libstagefrightSO = libStageFrightBAOS.toByteArray();

            KMPMatch binMatcher = new KMPMatch();

            int indexOf = binMatcher.indexOf(libstagefrightSO, "b/24445127".getBytes());
            boolean libstagefrightVulnerableToBug24445127 = indexOf == -1;

            indexOf = binMatcher.indexOf(libstagefrightSO, "bogus max input size: %zu".getBytes());
            boolean libstagefrightVulnerableToBug17769851 = indexOf == -1;

            indexOf = binMatcher.indexOf(libstagefrightSO, "b/24441553, b/24445122".getBytes());
            boolean libstagefrightVulnerableToBug24441553 = indexOf == -1;


            boolean is_vul = libstagefrightVulnerableToBug24445127 ||
                    libstagefrightVulnerableToBug17769851 ||
                    libstagefrightVulnerableToBug24441553;

            if(is_vul){
                Tester.apk_crash();
                Log.i(tag,"crash");
            }else{
                Tester.apk_done();
                Log.i(tag,"run ok ");
            }
        }catch(Exception e){
            e.printStackTrace();
            Tester.apk_done();
        }

    }
}

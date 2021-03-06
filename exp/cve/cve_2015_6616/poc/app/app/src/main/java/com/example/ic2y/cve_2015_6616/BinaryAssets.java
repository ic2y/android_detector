package com.example.ic2y.cve_2015_6616;


import android.content.Context;
import android.content.res.AssetManager;
import android.util.Log;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class BinaryAssets {

    private static final String TAG = BinaryAssets.class.getSimpleName();

    public static void extractAsset(Context ctx, String name, String destination) throws IOException {
        extractAsset(ctx, name, destination, true);
    }

    public static String extractAsset(Context ctx, String name) throws IOException {
        AssetManager assetManager = ctx.getAssets();
        InputStream asset = assetManager.open(name);
        ByteArrayOutputStream fos = new ByteArrayOutputStream();
        copy(asset, fos);
        return fos.toString();
    }

    public static void extractAsset(Context ctx, String name, String destination, boolean overwrite) throws IOException {
        Log.d(TAG, "Extracting \'" + name + "\' from assets to \'" + destination + "\' ...");

        try {
            File f = new File(destination);
            if(f.exists() && overwrite) {
                f.delete();
            }
        }

        catch(Exception e) {e.printStackTrace();}

        AssetManager assetManager = ctx.getAssets();
        InputStream asset = assetManager.open(name);
        FileOutputStream fos = new FileOutputStream(destination);
        copy(asset,fos);
    }

    public static void extractZipAsset(Context ctx, String zipAsset, String destination) throws IOException {
        AssetManager assetManager = ctx.getAssets();
        InputStream asset = assetManager.open(zipAsset);
        ZipInputStream zis = new ZipInputStream(asset);

        File extractionDir = new File(destination);

        boolean directionCreationSucceeded = extractionDir.mkdirs();

        ZipEntry ze = null;
        byte[] buffer = new byte[8192];
        while ((ze = zis.getNextEntry()) != null) {

            if(ze.isDirectory()){
                continue;
            }

            //Strip everything from the last '/'
            String zeName = ze.getName();
            String fileName = zeName;
            if(zeName.lastIndexOf('/') != -1){
                fileName = zeName.substring(zeName.lastIndexOf('/'), zeName.length());
            }

            String fileExtractionPath = destination + fileName;
            FileOutputStream fos = new FileOutputStream(fileExtractionPath);
            int len;
            while ((len = zis.read(buffer)) != -1) {
                fos.write(buffer, 0, len);
            }
            fos.close();
        }
    }

    private static final int BUFFER_SIZE = 2 * 1024 * 1024;
    public static void copy(InputStream input, OutputStream output) throws IOException {
        try {
            byte[] buffer = new byte[BUFFER_SIZE];
            int bytesRead = input.read(buffer);
            while (bytesRead != -1) {
                output.write(buffer, 0, bytesRead);
                bytesRead = input.read(buffer);
            }
            //If needed, close streams.
        } finally {
            input.close();
            output.close();
        }
    }
}
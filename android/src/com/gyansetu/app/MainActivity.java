package com.gyansetu.app;

import android.app.Activity;
import android.os.Bundle;
import android.view.WindowManager;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.graphics.Color;
import android.view.View;
import android.view.Window;

public class MainActivity extends Activity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // ====================================================================
        // 1. HARDWARE-ENFORCED DRM & ANTI-SCREENSHOT/ANTI-RECORDING SHIELD
        // ====================================================================
        // OS blocks screenshot key combinations & screen recording capture sinks
        getWindow().setFlags(
            WindowManager.LayoutParams.FLAG_SECURE,
            WindowManager.LayoutParams.FLAG_SECURE
        );

        // 2. Immersive Cosmic Navy Window styling
        Window window = getWindow();
        window.setStatusBarColor(Color.parseColor("#071322"));
        window.setNavigationBarColor(Color.parseColor("#071322"));

        setContentView(R.layout.activity_main);

        // 3. Secure WebView Setup
        webView = findViewById(R.id.webview);
        webView.setBackgroundColor(Color.parseColor("#071322"));

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setAllowFileAccessFromFileURLs(true);
        settings.setAllowUniversalAccessFromFileURLs(true);
        settings.setMediaPlaybackRequiresUserGesture(false);
        settings.setCacheMode(WebSettings.LOAD_NO_CACHE);

        // Keep all navigation sandboxed within the secured activity
        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                if (url.startsWith("file:///android_asset/")) {
                    view.loadUrl(url);
                    return true;
                }
                return false;
            }
        });

        webView.setWebChromeClient(new WebChromeClient());

        // 4. Load the sandboxed offline GyanSetu app bundle
        webView.loadUrl("file:///android_asset/index.html");
    }

    @Override
    public void onBackPressed() {
        if (webView != null && webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}

package com.mgg.pequenodavante;

import android.os.Bundle;
import android.graphics.Color;
import androidx.activity.EdgeToEdge;
import androidx.activity.SystemBarStyle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import com.mgg.pequenodavante.databinding.ActivityInicioSesionBinding;

public class InicioSesionActivity extends AppCompatActivity {
    private ActivityInicioSesionBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this,
                SystemBarStyle.light(Color.TRANSPARENT, Color.TRANSPARENT),
                SystemBarStyle.light(Color.TRANSPARENT, Color.TRANSPARENT));
        binding = ActivityInicioSesionBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        binding.guiaMarcaFotografia.setGuidelinePercent(
                getResources().getFraction(R.fraction.proporcion_marca, 1, 1));
        binding.lyIdentidadMarcaCentro.setClipToOutline(true);
        ViewCompat.setOnApplyWindowInsetsListener(binding.main, (view, windowInsets) -> {
            Insets bars = windowInsets.getInsets(WindowInsetsCompat.Type.systemBars());
            Insets keyboard = windowInsets.getInsets(WindowInsetsCompat.Type.ime());
            view.setPadding(bars.left, bars.top, bars.right, Math.max(bars.bottom, keyboard.bottom));
            return windowInsets;
        });
        binding.btnVolver.setOnClickListener(view -> getOnBackPressedDispatcher().onBackPressed());
        binding.tvTextoTerminos.setOnClickListener(view -> binding.cbAceptarTerminos.toggle());
    }
}

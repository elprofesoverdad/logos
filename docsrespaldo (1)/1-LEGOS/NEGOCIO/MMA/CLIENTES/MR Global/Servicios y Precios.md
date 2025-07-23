    Installing Bash-UI hotkey:  => [B
daniel@daniel-IdeaPad-3-15IIL05:~$ cerrarVentanas
daniel@daniel-IdeaPad-3-15IIL05:~$ alsa
Usage: /sbin/alsa {unload|reload|force-unload|force-reload|suspend|resume}
daniel@daniel-IdeaPad-3-15IIL05:~$ audio
Orden «audio» no encontrada. Quizá quiso decir:
  la orden «aubio» del paquete deb «aubio-tools (0.4.9-4.1build2)»
Pruebe con: sudo apt install <nombre del paquete deb>
daniel@daniel-IdeaPad-3-15IIL05:~$ pulseaudio -k
daniel@daniel-IdeaPad-3-15IIL05:~$ pulseaudio --start
daniel@daniel-IdeaPad-3-15IIL05:~$ pulseaudio -k
daniel@daniel-IdeaPad-3-15IIL05:~$ pulseaudio --start
daniel@daniel-IdeaPad-3-15IIL05:~$ sudo systemctl --user restart pulseaudio.service
[sudo] contraseña para daniel: 
Failed to connect to bus: $DBUS_SESSION_BUS_ADDRESS and $XDG_RUNTIME_DIR not defined (consider using --machine=<user>@.host --user to connect to bus of other user)
daniel@daniel-IdeaPad-3-15IIL05:~$ systemctl --user restart pulseaudio.service
daniel@daniel-IdeaPad-3-15IIL05:~$ sudo modprobe -r snd_hda_intel
modprobe: FATAL: Module snd_hda_intel is in use.
daniel@daniel-IdeaPad-3-15IIL05:~$ sudo modprobe snd_hda_intel
daniel@daniel-IdeaPad-3-15IIL05:~$ aplay -l
**** Lista de PLAYBACK dispositivos hardware ****
tarjeta 0: PCH [HDA Intel PCH], dispositivo 3: HDMI 0 [HDMI 0]
  Subdispositivos: 1/1
  Subdispositivo #0: subdevice #0
tarjeta 0: PCH [HDA Intel PCH], dispositivo 7: HDMI 1 [HDMI 1]
  Subdispositivos: 1/1
  Subdispositivo #0: subdevice #0
tarjeta 0: PCH [HDA Intel PCH], dispositivo 8: HDMI 2 [HDMI 2]
  Subdispositivos: 1/1
  Subdispositivo #0: subdevice #0
tarjeta 0: PCH [HDA Intel PCH], dispositivo 9: HDMI 3 [HDMI 3]
  Subdispositivos: 1/1
  Subdispositivo #0: subdevice #0
daniel@daniel-IdeaPad-3-15IIL05:~$ lsmod | grep snd
snd_hda_codec_hdmi     94208  1
snd_sof_pci_intel_icl    12288  0
snd_sof_intel_hda_common   200704  1 snd_sof_pci_intel_icl
soundwire_intel        65536  1 snd_sof_intel_hda_common
snd_sof_intel_hda_mlink    45056  2 soundwire_intel,snd_sof_intel_hda_common
snd_sof_intel_hda      24576  1 snd_sof_intel_hda_common
snd_sof_pci            24576  2 snd_sof_pci_intel_icl,snd_sof_intel_hda_common
snd_sof_xtensa_dsp     12288  1 snd_sof_intel_hda_common
snd_sof               360448  3 snd_sof_pci,snd_sof_intel_hda_common,snd_sof_intel_hda
snd_sof_utils          16384  1 snd_sof
snd_soc_hdac_hda       24576  1 snd_sof_intel_hda_common
snd_hda_ext_core       36864  4 snd_sof_intel_hda_common,snd_soc_hdac_hda,snd_sof_intel_hda_mlink,snd_sof_intel_hda
snd_soc_acpi_intel_match    94208  2 snd_sof_pci_intel_icl,snd_sof_intel_hda_common
snd_soc_acpi           12288  2 snd_soc_acpi_intel_match,snd_sof_intel_hda_common
snd_soc_core          446464  4 soundwire_intel,snd_sof,snd_sof_intel_hda_common,snd_soc_hdac_hda
snd_compress           28672  1 snd_soc_core
ac97_bus               12288  1 snd_soc_core
snd_pcm_dmaengine      16384  1 snd_soc_core
snd_hda_intel          61440  1
snd_intel_dspcfg       32768  3 snd_hda_intel,snd_sof,snd_sof_intel_hda_common
snd_intel_sdw_acpi     16384  2 snd_sof_intel_hda_common,snd_intel_dspcfg
snd_hda_codec         212992  4 snd_hda_codec_hdmi,snd_hda_intel,snd_soc_hdac_hda,snd_sof_intel_hda
snd_hda_core          147456  7 snd_hda_codec_hdmi,snd_hda_intel,snd_hda_ext_core,snd_hda_codec,snd_sof_intel_hda_common,snd_soc_hdac_hda,snd_sof_intel_hda
snd_hwdep              20480  1 snd_hda_codec
snd_pcm               196608  11 snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec,soundwire_intel,snd_sof,snd_sof_intel_hda_common,snd_compress,snd_soc_core,snd_sof_utils,snd_hda_core,snd_pcm_dmaengine
snd_seq_midi           24576  0
snd_seq_midi_event     16384  1 snd_seq_midi
snd_rawmidi            57344  1 snd_seq_midi
snd_seq               118784  2 snd_seq_midi,snd_seq_midi_event
snd_seq_device         16384  3 snd_seq,snd_seq_midi,snd_rawmidi
snd_timer              49152  2 snd_seq,snd_pcm
snd                   143360  14 snd_seq,snd_seq_device,snd_hda_codec_hdmi,snd_hwdep,snd_hda_intel,snd_hda_codec,snd_sof,snd_timer,snd_compress,snd_soc_core,snd_pcm,snd_rawmidi
soundcore              16384  1 snd
daniel@daniel-IdeaPad-3-15IIL05:~$ sudo modprobe snd_hda_intel
daniel@daniel-IdeaPad-3-15IIL05:~$ dmesg | grep -i audio
dmesg: fallo al leer el «buffer» del núcleo: Operación no permitida
daniel@daniel-IdeaPad-3-15IIL05:~$ sudo dmesg | grep -i audio
[   25.441832] snd_hda_intel 0000:00:1f.3: bound 0000:00:02.0 (ops i915_audio_component_bind_ops [i915])
daniel@daniel-IdeaPad-3-15IIL05:~$ 


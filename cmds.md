# Commands

## Command to check audio devices

```powershell
ffmpeg -list_devices true -f dshow -i dummy
```

## Version

```powershell
ffmpeg -version
```

## Cut 1s from start

```powershell
ffmpeg -i input.mp4 -ss 00:00:01 -c copy output.mp4
```

## Video duration

```powershell
ffmpeg -i input.mp4
```

## Cut 1s from end

```powershell
ffmpeg -i input.mp4 -t 00:02:29.00 -c copy output.mp4
```

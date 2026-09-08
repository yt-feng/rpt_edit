# Research PDF assets

Loaded on demand by the research exporter and served from the same site. No report data or chart bytes are sent to a third-party conversion service.

- pdf-lib 1.17.1: https://github.com/Hopding/pdf-lib (MIT; license alongside).
- @pdf-lib/fontkit 1.1.1: https://github.com/Hopding/fontkit (MIT; upstream README with license declaration alongside).
- Research Sans Regular: a static weight-400 TrueType derivative of Noto Sans SC Variable, renamed to avoid using reserved names for modified fonts. Source: https://github.com/notofonts/noto-cjk/blob/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf (SIL Open Font License 1.1; OFL.txt alongside).

The font filename carries its SHA-256 prefix. Library filenames pin the version. Keep these immutable and change filenames when updating bytes. The font is 10.6 MB and loaded only when PDF export is requested. Full TrueType embedding is intentional: the fontkit CJK subset path dropped glyphs during Poppler visual verification. A typical text-and-one-chart PDF is around 6.5 MB. Chinese text stays searchable and selectable.

The static font was instantiated with fonttools 4.64.0 at wght=400; name IDs 1/2/3/4/6/16/17 were changed to the derivative family and style. Keep original copyright and license records. No installed system font was copied.

## SHA-256

- `ResearchSans-Regular-a08975ee9c1e.ttf`: `a08975ee9c1eee635eea6cbf6529f5a59b8544c59748d963b82ee263dac5785d`
- `fontkit-1.1.1.min.js`: `d8df561b9fba98e24f2e5130e40948809281bbbc55a20c412359f1a0a5eb35a6`
- `pdf-lib-1.17.1.min.js`: `0f9a5cad07941f0826586c94e089d89b918c46e5c17cf2d5a3c6f666e3bc694f`

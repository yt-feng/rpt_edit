import { qrcodegen } from "./vendor/qrcodegen.js";

// The source uses an opaque WeChat login ticket. Encode its exact bytes locally;
// never put the ticket into an external image-service URL, logs, or SVG markup.
export function reportifyQrDataUrl(value) {
  if (typeof value !== "string" || !value || value.length > 256
    || new TextEncoder().encode(value).length > 256
    || /[\s\x00-\x1f\x7f]/u.test(value)
    || !/^https?:\/\/weixin\.qq\.com\/q\/[^/?#\\]+$/u.test(value)) throw new Error("Invalid login QR payload.");
  let url;
  try { url = new URL(value); } catch (_error) { throw new Error("Invalid login QR payload."); }
  if (!["http:", "https:"].includes(url.protocol) || url.hostname !== "weixin.qq.com"
    || url.username || url.password || url.port || !/^\/q\/[^/]+$/u.test(url.pathname)
    || url.hash || url.search) throw new Error("Invalid login QR payload.");

  const qr = qrcodegen.QrCode.encodeText(value, qrcodegen.QrCode.Ecc.MEDIUM);
  const border = 4;
  const dimension = qr.size + border * 2;
  const modules = [];
  for (let y = 0; y < qr.size; y += 1) {
    for (let x = 0; x < qr.size; x += 1) {
      if (qr.getModule(x, y)) modules.push(`M${x + border},${y + border}h1v1h-1z`);
    }
  }
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320" viewBox="0 0 ${dimension} ${dimension}" shape-rendering="crispEdges"><rect width="100%" height="100%" fill="white"/><path d="${modules.join("")}" fill="black"/></svg>`;
  return `data:image/svg+xml;base64,${btoa(svg)}`;
}

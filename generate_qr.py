import os
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_eye_catching_qr(url, out_clean_path, logo_path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=14,
        border=3
    )
    qr.add_data(url)
    qr.make(fit=True)

    matrix = qr.get_matrix()
    matrix_size = len(matrix)
    box_size = 14
    qr_img_size = matrix_size * box_size

    # Cosmic Navy Backdrop
    qr_img = Image.new("RGBA", (qr_img_size, qr_img_size), (7, 19, 34, 255))
    draw = ImageDraw.Draw(qr_img)

    def is_finder_pattern(r, c):
        if r < 8 and c < 8:
            return True
        if r < 8 and c >= matrix_size - 8:
            return True
        if r >= matrix_size - 8 and c < 8:
            return True
        return False

    # Draw data modules with vibrant gradient & smooth rounded corners
    for r in range(matrix_size):
        for c in range(matrix_size):
            if matrix[r][c]:
                x1 = c * box_size
                y1 = r * box_size
                x2 = x1 + box_size
                y2 = y1 + box_size

                ratio = (r + c) / (2.0 * matrix_size)
                
                if is_finder_pattern(r, c):
                    color = (255, 160, 72, 255) if ratio < 0.5 else (80, 190, 180, 255)
                    draw.rectangle([x1, y1, x2, y2], fill=color)
                else:
                    red = int(255 * (1 - ratio) + 80 * ratio)
                    green = int(160 * (1 - ratio) + 175 * ratio)
                    blue = int(72 * (1 - ratio) + 165 * ratio)
                    draw.rounded_rectangle([x1 + 1, y1 + 1, x2 - 1, y2 - 1], radius=3, fill=(red, green, blue, 255))

    # Center Logo with Glowing Circular Badge
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo_size = int(qr_img_size * 0.23)
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        mask = Image.new("L", (logo_size, logo_size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, logo_size, logo_size), fill=255)

        badge_pad = 12
        badge_size = logo_size + badge_pad * 2
        badge = Image.new("RGBA", (badge_size, badge_size), (0, 0, 0, 0))
        badge_draw = ImageDraw.Draw(badge)
        
        # Outer glow
        badge_draw.ellipse([0, 0, badge_size, badge_size], fill=(80, 155, 147, 80))
        # Inner solid base
        badge_draw.ellipse([3, 3, badge_size - 3, badge_size - 3], fill=(7, 19, 34, 255), outline=(255, 160, 72, 255), width=3)

        badge.paste(logo, (badge_pad, badge_pad), mask)

        bx = (qr_img_size - badge_size) // 2
        by = (qr_img_size - badge_size) // 2
        qr_img.paste(badge, (bx, by), badge)

    qr_img.save(out_clean_path, "PNG")
    print(f"Generated Eye-Catching QR: {out_clean_path}")
    return qr_img

def create_showcase_card(qr_img, display_url, out_card_path):
    card_w = 1000
    card_h = 1380
    poster = Image.new("RGBA", (card_w, card_h), (5, 14, 26, 255))
    pdraw = ImageDraw.Draw(poster)

    teal_orb = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(teal_orb)
    tdraw.ellipse([card_w - 300, -100, card_w + 300, 500], fill=(80, 155, 147, 70))
    tdraw.ellipse([-150, card_h - 450, 450, card_h + 150], fill=(249, 124, 34, 55))
    teal_orb = teal_orb.filter(ImageFilter.GaussianBlur(80))
    poster = Image.alpha_composite(poster, teal_orb)
    pdraw = ImageDraw.Draw(poster)

    pad_x = 70
    card_top = 80
    card_bottom = card_h - 80
    pdraw.rounded_rectangle(
        [pad_x, card_top, card_w - pad_x, card_bottom],
        radius=36,
        fill=(10, 27, 46, 235),
        outline=(255, 255, 255, 45),
        width=2
    )

    pdraw.line([pad_x + 36, card_top + 1, card_w - pad_x - 36, card_top + 1], fill=(255, 255, 255, 140), width=2)

    font_paths = [
        r"C:\Windows\Fonts\segoeuib.ttf",
        r"C:\Windows\Fonts\arialbd.ttf",
    ]
    font_bold_path = font_paths[0] if os.path.exists(font_paths[0]) else "arial.ttf"
    font_reg_path = r"C:\Windows\Fonts\segoeui.ttf" if os.path.exists(r"C:\Windows\Fonts\segoeui.ttf") else "arial.ttf"

    font_title = ImageFont.truetype(font_bold_path, 46)
    font_sub = ImageFont.truetype(font_bold_path, 20)
    font_lead = ImageFont.truetype(font_reg_path, 22)
    font_url = ImageFont.truetype(font_bold_path, 22)
    font_badge = ImageFont.truetype(font_bold_path, 18)
    font_credit = ImageFont.truetype(font_reg_path, 18)

    pill_text = "● LIVE BROADCAST & STREAM"
    pdraw.rounded_rectangle([card_w//2 - 170, card_top + 45, card_w//2 + 170, card_top + 85], radius=20, fill=(249, 124, 34, 35), outline=(249, 124, 34, 120), width=1)
    pdraw.text((card_w//2, card_top + 65), pill_text, fill=(255, 160, 72, 255), font=font_badge, anchor="mm")

    pdraw.text((card_w//2, card_top + 130), "GYANSETU", fill=(255, 255, 255, 255), font=font_title, anchor="mm")
    pdraw.text((card_w//2, card_top + 175), "Global Internet Radio Station", fill=(101, 168, 160, 255), font=font_sub, anchor="mm")
    pdraw.text((card_w//2, card_top + 215), "Demystifying Hard Topics • Igniting Curiosity", fill=(180, 195, 210, 255), font=font_lead, anchor="mm")

    qr_scale_size = 540
    qr_resized = qr_img.resize((qr_scale_size, qr_scale_size), Image.LANCZOS)
    
    qr_frame_pad = 18
    qf_x1 = (card_w - qr_scale_size) // 2 - qr_frame_pad
    qf_y1 = card_top + 265
    qf_x2 = qf_x1 + qr_scale_size + qr_frame_pad * 2
    qf_y2 = qf_y1 + qr_scale_size + qr_frame_pad * 2

    # Glowing backplate
    pdraw.rounded_rectangle([qf_x1, qf_y1, qf_x2, qf_y2], radius=28, fill=(7, 19, 34, 255), outline=(80, 155, 147, 90), width=2)
    poster.paste(qr_resized, (qf_x1 + qr_frame_pad, qf_y1 + qr_frame_pad), qr_resized)

    c_y = qf_y2 + 35
    pdraw.text((card_w//2, c_y), "Point camera to listen instantly on any phone", fill=(255, 255, 255, 255), font=font_sub, anchor="mm")

    url_pill_y = c_y + 40
    clean_url = display_url.replace("https://", "").replace("/", "")
    pdraw.rounded_rectangle([card_w//2 - 260, url_pill_y - 22, card_w//2 + 260, url_pill_y + 22], radius=22, fill=(80, 155, 147, 30), outline=(80, 155, 147, 100), width=1)
    pdraw.text((card_w//2, url_pill_y), clean_url, fill=(255, 190, 100, 255), font=font_url, anchor="mm")

    feats_y = url_pill_y + 55
    feats_text = "Zero Paywalls   •   7 Full Episodes   •   215+ Global Streams   •   Android App"
    pdraw.text((card_w//2, feats_y), feats_text, fill=(155, 180, 205, 255), font=font_credit, anchor="mm")

    # Founders Credit
    pdraw.line([pad_x + 50, card_bottom - 75, card_w - pad_x - 50, card_bottom - 75], fill=(255, 255, 255, 25), width=1)
    pdraw.text((card_w//2, card_bottom - 42), "Simran Ailani (Founder & Lead Host)  •  Tanmay Rambhau Thakre (Technical Architect & Co-Founder)", fill=(130, 155, 175, 255), font=font_credit, anchor="mm")

    poster.save(out_card_path, "PNG")
    print(f"Saved Showcase Poster: {out_card_path}")

def main():
    base_dir = r"c:\Users\hp\OneDrive\Desktop\gyan setu"
    logo_path = os.path.join(base_dir, "assets", "images", "logo.png")
    
    url_vercel = "https://gyansetu-five.vercel.app/"
    url_netlify = "https://imaginative-centaur-0c2b59.netlify.app/"
    
    path_vercel = os.path.join(base_dir, "assets", "images", "gyansetu_qr_vercel.png")
    path_netlify = os.path.join(base_dir, "assets", "images", "gyansetu_qr_netlify.png")
    path_legacy = os.path.join(base_dir, "assets", "images", "gyansetu_qr_code.png")

    poster_vercel = os.path.join(base_dir, "assets", "images", "gyansetu_qr_showcase_vercel.png")
    poster_netlify = os.path.join(base_dir, "assets", "images", "gyansetu_qr_showcase_netlify.png")
    poster_legacy = os.path.join(base_dir, "assets", "images", "gyansetu_qr_showcase.png")

    # Generate both eye-catching QR codes
    qr_v = create_eye_catching_qr(url_vercel, path_vercel, logo_path)
    qr_n = create_eye_catching_qr(url_netlify, path_netlify, logo_path)
    qr_v.save(path_legacy, "PNG")

    create_showcase_card(qr_v, url_vercel, poster_vercel)
    create_showcase_card(qr_n, url_netlify, poster_netlify)
    create_showcase_card(qr_v, url_vercel, poster_legacy)

if __name__ == "__main__":
    main()

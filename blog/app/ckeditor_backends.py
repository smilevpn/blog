from ckeditor_uploader.backends import PillowBackend
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class CompressingPillowBackend(PillowBackend):
    def process_image(self, uploaded_file):
        # 1. Открываем картинку через Pillow
        img = Image.open(uploaded_file)
        
        # 2. Конвертируем в RGB (если это PNG с прозрачностью)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # 3. Уменьшаем размер до 1600px по ширине
        if img.width > 1600:
            output_size = (1600, int(img.height * (1600 / img.width)))
            img = img.resize(output_size, Image.Resampling.LANCZOS)
        
        # 4. Сохраняем в буфер с качеством 80
        output = BytesIO()
        img.save(output, format='JPEG', quality=80, optimize=True)
        output.seek(0)
        
        # 5. Возвращаем новый файл с расширением .jpg
        new_name = uploaded_file.name.rsplit('.', 1)[0] + '.jpg'
        return ContentFile(output.read(), name=new_name)

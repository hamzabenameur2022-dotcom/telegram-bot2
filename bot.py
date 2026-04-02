
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# خذ التوكن من المتغيرات البيئية (من Render)
TOKEN = os.environ.get("8732588517:AAGzwNWGKDfr9dFwwgcBwqV9SC7A4Ur75uk")

# دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_msg = """
🤖 أهلاً بك في بوت الدروب شيبينغ!

الأوامر المتاحة:
/profit - حاسبة الأرباح
/products - منتجات مقترحة
/supplier - معلومات عن الموردين
/help - المساعدة
"""
    await update.message.reply_text(welcome_msg)

# حاسبة الأرباح
async def profit_calculator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧮 حاسبة الأرباح\n\n"
        "أرسل لي:\n"
        "سعر المنتج, سعر الشحن, نسبة الربح المطلوبة\n\n"
        "مثال: 10, 2, 30"
    )
    context.user_data['waiting_for_profit'] = True

async def calculate_profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('waiting_for_profit'):
        try:
            data = update.message.text.split(',')
            product_price = float(data[0])
            shipping = float(data[1])
            profit_margin = float(data[2])
            
            total_cost = product_price + shipping
            selling_price = total_cost + (total_cost * profit_margin / 100)
            profit = selling_price - total_cost
            
            result = f"""
💰 نتيجة الحساب:

سعر المنتج: ${product_price}
الشحن: ${shipping}
التكلفة الكلية: ${total_cost}
هامش الربح: {profit_margin}%
✅ سعر البيع المقترح: ${selling_price:.2f}💵 الربح: ${profit:.2f}
"""
            await update.message.reply_text(result)
        except:
            await update.message.reply_text("❌ خطأ في البيانات. حاول مرة أخرى.")
        
        context.user_data['waiting_for_profit'] = False

# منتجات مقترحة
async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = """
🔥 منتجات مقترحة للدروب شيبينغ:

1️⃣ إكسسوارات الهواتف
   - سعر الشراء: $1-3
   - سعر البيع: $10-15
   - الربح: 300-400%

2️⃣ أدوات المطبخ الذكية
   - سعر الشراء: $3-5
   - سعر البيع: $15-20
   - الربح: 200-300%

3️⃣ منتجات العناية بالبشرة
   - سعر الشراء: $2-4
   - سعر البيع: $12-18
   - الربح: 250-350%

💡 ابحث عن هذه المنتجات على:
• AliExpress.com
• Alibaba.com
• CJdropshipping.com
"""
    await update.message.reply_text(msg)

# معلومات الموردين
async def supplier_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = """
📦 أفضل الموردين المجانيين:

1️⃣ **AliExpress**
   ✅ لا حد أدنى للطلب
   ✅ شحن مجاني لبعض المنتجات
   ⚠️ وقت شحن طويل (15-30 يوم)

2️⃣ **CJdropshipping**
   ✅ أسرع من AliExpress
   ✅ فحص جودة مجاني
   ✅ تخزين مجاني
3️⃣ **AliDropship**
   ✅ متخصص في الدروب شيبينغ
   ✅ أسعار تنافسية

💡 نصيحة: ابدأ بـ AliExpress لأنه الأسهل!
"""
    await update.message.reply_text(msg)

# المساعدة
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_msg = """
📚 كيفية استخدام البوت:

1. استخدم /profit لحساب أرباحك
2. استخدم /products لرؤية منتجات مقترحة
3. استخدم /supplier لمعرفة أفضل الموردين
4. استخدم /start للعودة للقائمة الرئيسية

🎯 نصائح مهمة:
• ابحث عن منتجات بهامش ربح 3x على الأقل
• ركز على المنتجات الخفيفة (شحن أرخص)
• تجنب المنتجات الكبيرة والثقيلة
• اختبر المنتج قبل الاستثمار الكبير

💰 كيف تربح؟
1. ابحث عن منتج رائج
2. احسب الربح باستخدام البوت
3. أنشئ متجر على Shopify أو WooCommerce
4. روّج للمنتج على وسائل التواصل
5. عندما يشتري العميل، اطلب من المورد
6. الربح هو الفرق!
"""
    await update.message.reply_text(help_msg)

# الدالة الرئيسية
def main():
    app = Application.builder().token(TOKEN).build()
    
    # إضافة المعالجات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profit", profit_calculator))
    app.add_handler(CommandHandler("products", products))
    app.add_handler(CommandHandler("supplier", supplier_info))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate_profit))
    
    print("🤖 البوت يعمل الآن...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':    main()

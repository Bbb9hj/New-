from flask import Flask, render_template_string
import os

app = Flask(__name__)

# واجهة التطبيق كاملة (HTML + CSS + React)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Psychiatry Index - الدفعة السادسة</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://unpkg.com/framer-motion@10.16.4/dist/framer-motion.js"></script>
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #f9fafb; }
        .glass-card { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); }
    </style>
</head>
<body>
    <div id="root"></div>

    <script>
        const { useState, useMemo, useEffect } = React;
        const { motion, AnimatePresence } = FramerMotion;

        const PSYCHIATRY_DATA = [
            { id: 1, title: "Psychiatric assessment", doctor: "د. علي الأكوع", report: "https://t.me/September216thbatchpsychiatry/8", recording: "https://t.me/September216thbatchpsychiatry/10?single", material: "https://t.me/September216thbatchpsychiatry/12?single" },
            { id: 2, title: "Organic and substance disorders", doctor: "د. علي الأكوع", report: "https://t.me/September216thbatchpsychiatry/9", recording: "https://t.me/September216thbatchpsychiatry/11?single", material: "https://t.me/September216thbatchpsychiatry/14?single" },
            { id: 3, title: "Anxiety disorder", doctor: "د. تسنيم القبيلي", report: "https://t.me/September216thbatchpsychiatry/4", recording: "https://t.me/September216thbatchpsychiatry/5?single", material: "https://t.me/September216thbatchpsychiatry/7" },
            { id: 4, title: "Somatic disorders", doctor: "د. تسنيم القبيلي", report: "https://t.me/September216thbatchpsychiatry/39", recording: "https://t.me/September216thbatchpsychiatry/40", material: "https://t.me/September216thbatchpsychiatry/78" },
            { id: 5, title: "Schizophrenia and psychosis", doctor: "د. فكري النائب", report: "https://t.me/September216thbatchpsychiatry/24", recording: "https://t.me/September216thbatchpsychiatry/31", material: "https://t.me/September216thbatchpsychiatry/26?single" },
            { id: 6, title: "Mood disorders", doctor: "د. فكري النائب", report: "https://t.me/September216thbatchpsychiatry/32", recording: "https://t.me/September216thbatchpsychiatry/35", material: "https://t.me/September216thbatchpsychiatry/34?single" },
            { id: 7, title: "Sleep and Sexual disorders", doctor: "د. فكري النائب", report: "https://t.me/September216thbatchpsychiatry/18", recording: "https://t.me/September216thbatchpsychiatry/22", material: "https://t.me/September216thbatchpsychiatry/20?single" },
            { id: 8, title: "Personality disorders", doctor: "د. فكري النائب", report: "https://t.me/September216thbatchpsychiatry/18", recording: "https://t.me/September216thbatchpsychiatry/22", material: "https://t.me/September216thbatchpsychiatry/20?single" },
            { id: 9, title: "Child Psychiatry and Dissociative disorders", doctor: "د. فكري النائب", report: "https://t.me/September216thbatchpsychiatry/44", recording: "https://t.me/September216thbatchpsychiatry/45", material: "https://t.me/September216thbatchpsychiatry/47?single" }
        ];

        function App() {
            const [view, setView] = useState('splash');
            const [searchQuery, setSearchQuery] = useState('');

            useEffect(() => { lucide.createIcons(); }, [view, searchQuery]);

            const filteredLectures = useMemo(() => {
                return PSYCHIATRY_DATA.filter(l => l.title.toLowerCase().includes(searchQuery.toLowerCase()) || l.doctor.includes(searchQuery));
            }, [searchQuery]);

            return React.createElement('div', { className: "min-h-screen max-w-lg mx-auto bg-gray-50 pb-20 select-none" },
                React.createElement(AnimatePresence, { mode: "wait" },
                    view === 'splash' ? React.createElement(motion.div, { 
                        initial: { opacity: 0 }, animate: { opacity: 1 }, exit: { opacity: 0 },
                        className: "flex flex-col items-center justify-center h-screen p-8 text-center"
                    },
                        React.createElement('div', { className: "mb-10 p-8 bg-white rounded-full shadow-2xl" }, 
                            React.createElement('i', { 'data-lucide': 'brain-circuit', className: "w-20 h-20 text-orange-500" })),
                        React.createElement('h1', { className: "text-3xl font-bold mb-4" }, "✨ فهرس قسم الـ Psychiatry ✨"),
                        React.createElement('p', { className: "text-gray-500 mb-10" }, "مرحباً بكم في تطبيق الفهرس الشامل للدفعة السادسة"),
                        React.createElement('button', { 
                            onClick: () => setView('index'),
                            className: "w-full py-4 bg-orange-500 text-white rounded-2xl font-bold shadow-lg"
                        }, "ابدأ التصفح")
                    ) : 
                    React.createElement(motion.div, { initial: { opacity: 0 }, animate: { opacity: 1 }, className: "p-4" },
                        React.createElement('div', { className: "flex justify-between items-center mb-6" },
                            React.createElement('h2', { className: "text-xl font-bold" }, "فهرس المحاضرات"),
                            React.createElement('i', { 'data-lucide': 'layout-grid', className: "text-orange-500" })
                        ),
                        React.createElement('div', { className: "relative mb-6" },
                            React.createElement('input', {
                                type: "text", placeholder: "ابحث هنا...",
                                className: "w-full p-4 pr-12 rounded-2xl border-none shadow-sm outline-none",
                                onChange: (e) => setSearchQuery(e.target.value)
                            }),
                            React.createElement('i', { 'data-lucide': 'search', className: "absolute right-4 top-4 text-gray-400" })
                        ),
                        filteredLectures.map(l => React.createElement('div', { key: l.id, className: "bg-white p-5 rounded-[2rem] shadow-sm mb-4 border border-gray-100" },
                            React.createElement('div', { className: "flex items-start gap-4 mb-5" },
                                React.createElement('div', { className: "bg-orange-500 text-white w-8 h-8 rounded-lg flex items-center justify-center font-bold" }, l.id),
                                React.createElement('div', null, 
                                    React.createElement('h3', { className: "font-bold text-gray-800" }, l.title),
                                    React.createElement('p', { className: "text-sm text-gray-400" }, l.doctor))
                            ),
                            React.createElement('div', { className: "grid grid-cols-4 gap-2 text-center" },
                                [['الملزمة', 'book-open', l.material, 'bg-blue-500'], ['التسجيل', 'mic', l.recording, 'bg-orange-500'], ['التقرير', 'file-text', l.report, 'bg-yellow-500'], ['التفريغ', 'layers', l.material, 'bg-green-500']]
                                .map(([label, icon, link, color]) => React.createElement('a', { href: link, target: "_blank", className: "flex flex-col items-center gap-1" },
                                    React.createElement('div', { className: `${color} w-12 h-12 rounded-xl flex items-center justify-center text-white shadow-sm` },
                                        React.createElement('i', { 'data-lucide': icon, className: "w-6 h-6" })),
                                    React.createElement('span', { className: "text-[10px] font-bold" }, label)
                                ))
                            )
                        ))
                    )
                ),
                view !== 'splash' && React.createElement('nav', { className: "fixed bottom-0 left-0 right-0 bg-white/80 backdrop-blur-md p-4 flex justify-around border-t" },
                    [['layout-grid', 'الرئيسية'], ['search', 'البحث'], ['user', 'حسابي']].map(([icon, label]) => React.createElement('div', { className: "flex flex-col items-center text-gray-400" },
                        React.createElement('i', { 'data-lucide': icon, className: "w-6 h-6" }),
                        React.createElement('span', { className: "text-[10px]" }, label)
                    ))
                )
            );
        }

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(React.createElement(App));
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
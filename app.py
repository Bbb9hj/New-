from flask import Flask, render_template_string

app = Flask(__name__)

# بيانات المحاضرات (Data)
LECTURES_DATA = [
    {
        "id": 1,
        "title": "Psychiatric assessment",
        "doctor": "د. علي الأكوع",
        "report": "https://t.me/September216thbatchpsychiatry/8",
        "recording": "https://t.me/September216thbatchpsychiatry/10?single",
        "material": "https://t.me/September216thbatchpsychiatry/12?single",
    },
    {
        "id": 2,
        "title": "Organic and substance disorders",
        "doctor": "د. علي الأكوع",
        "report": "https://t.me/September216thbatchpsychiatry/9",
        "recording": "https://t.me/September216thbatchpsychiatry/11?single",
        "material": "https://t.me/September216thbatchpsychiatry/14?single",
    },
    {
        "id": 3,
        "title": "Anxiety disorder",
        "doctor": "د. تسنيم القبيلي",
        "report": "https://t.me/September216thbatchpsychiatry/4",
        "recording": "https://t.me/September216thbatchpsychiatry/5?single",
        "material": "https://t.me/September216thbatchpsychiatry/7",
    },
    {
        "id": 4,
        "title": "Somatic disorders",
        "doctor": "د. تسنيم القبيلي",
        "report": "https://t.me/September216thbatchpsychiatry/39",
        "recording": "https://t.me/September216thbatchpsychiatry/40",
        "material": "https://t.me/September216thbatchpsychiatry/78",
    },
    {
        "id": 5,
        "title": "Schizophrenia and psychosis",
        "doctor": "د. فكري النائب",
        "report": "https://t.me/September216thbatchpsychiatry/24",
        "recording": "https://t.me/September216thbatchpsychiatry/31",
        "material": "https://t.me/September216thbatchpsychiatry/26?single",
    },
    {
        "id": 6,
        "title": "Mood disorders",
        "doctor": "د. فكري النائب",
        "report": "https://t.me/September216thbatchpsychiatry/32",
        "recording": "https://t.me/September216thbatchpsychiatry/35",
        "material": "https://t.me/September216thbatchpsychiatry/34?single",
    },
    {
        "id": 7,
        "title": "Sleep and Sexual disorders",
        "doctor": "د. فكري النائب",
        "report": "https://t.me/September216thbatchpsychiatry/18",
        "recording": "https://t.me/September216thbatchpsychiatry/22",
        "material": "https://t.me/September216thbatchpsychiatry/20?single",
    },
    {
        "id": 8,
        "title": "Personality disorders",
        "doctor": "د. فكري النائب",
        "report": "https://t.me/September216thbatchpsychiatry/18",
        "recording": "https://t.me/September216thbatchpsychiatry/22",
        "material": "https://t.me/September216thbatchpsychiatry/20?single",
    },
    {
        "id": 9,
        "title": "Child Psychiatry and Dissociative disorders",
        "doctor": "د. فكري النائب",
        "report": "https://t.me/September216thbatchpsychiatry/44",
        "recording": "https://t.me/September216thbatchpsychiatry/45",
        "material": "https://t.me/September216thbatchpsychiatry/47?single",
    }
]

# واجهة المستخدم (HTML/React Template)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Psychiatry Index - الدفعة السادسة</title>
    <!-- Fonts & Tailwind -->
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://unpkg.com/framer-motion@10.16.4/dist/framer-motion.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #fafafa; }
        .glass-card { background: rgba(255, 255, 255, 0.82); backdrop-filter: blur(10px); }
        .orange-shadow { shadow-color: rgba(249, 115, 22, 0.2); }
    </style>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: { primary: '#f97316', secondary: '#0ea5e9' }
                }
            }
        }
    </script>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useMemo, useEffect } = React;
        const { motion, AnimatePresence } = FramerMotion;

        const LECTURES = """ + str(LECTURES_DATA) + """;

        function App() {
            const [view, setView] = useState('splash');
            const [searchQuery, setSearchQuery] = useState('');

            const filteredLectures = useMemo(() => {
                return LECTURES.filter(l => 
                    l.title.toLowerCase().includes(searchQuery.toLowerCase()) || 
                    l.doctor.includes(searchQuery)
                );
            }, [searchQuery]);

            // Icons initialization
            useEffect(() => { lucide.createIcons(); }, [view, filteredLectures]);

            return (
                <div className="min-h-screen max-w-md mx-auto relative overflow-hidden pb-24">
                    <AnimatePresence mode="wait">
                        {view === 'splash' && (
                            <motion.div 
                                key="splash"
                                initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0, y: -20 }}
                                className="flex flex-col items-center justify-center min-h-screen p-8 text-center"
                            >
                                <div className="absolute top-0 right-0 w-32 h-32 bg-blue-500 rounded-bl-full opacity-10" />
                                <div className="absolute bottom-0 left-0 w-48 h-48 bg-orange-500 rounded-tr-full opacity-10" />
                                
                                <div className="relative mb-12">
                                    <div className="w-48 h-48 rounded-full border-8 border-orange-100 flex items-center justify-center bg-white shadow-2xl">
                                        <div className="grid grid-cols-2 gap-3">
                                            <div className="text-blue-500"><i data-lucide="book-open"></i></div>
                                            <div className="text-orange-500"><i data-lucide="mic"></i></div>
                                            <div className="text-green-500"><i data-lucide="file-text"></i></div>
                                            <div className="text-yellow-500"><i data-lucide="layers"></i></div>
                                        </div>
                                    </div>
                                </div>

                                <h1 className="text-3xl font-bold text-gray-800 mb-4">
                                     ✨ فهرس قسم الـ <span className="text-orange-500">Psychiatry</span> ✨
                                </h1>
                                <p className="text-gray-500 mb-12 leading-relaxed">
                                    مرحباً بكم في تطبيق الفهرس الشامل المعني بتنظيم محاضرات الطب النفسي للدفعة السادسة.
                                </p>

                                <button 
                                    onClick={() => setView('index')}
                                    className="w-full py-4 bg-orange-500 text-white rounded-2xl font-bold text-lg shadow-xl flex items-center justify-center gap-3 active:scale-95 transition-transform"
                                >
                                    ابدأ التصفح
                                    <i data-lucide="arrow-left" className="w-5 h-5"></i>
                                </button>
                                <p className="mt-8 text-sm font-semibold text-gray-400">اللجنة العلمية للدفعة السادسة</p>
                            </motion.div>
                        )}

                        {view === 'index' && (
                            <motion.div 
                                key="index"
                                initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }}
                                className="p-6"
                            >
                                <div className="flex items-center justify-between mb-8">
                                    <h2 className="text-2xl font-bold text-gray-800">فهرس المحاضرات</h2>
                                    <div className="w-10 h-10 rounded-xl bg-orange-100 flex items-center justify-center text-orange-500">
                                        <i data-lucide="layout-grid"></i>
                                    </div>
                                </div>

                                <div className="relative mb-8">
                                    <input 
                                        type="text" 
                                        placeholder="ابحث عن محاضرة أو طبيب..."
                                        className="w-full bg-white border-0 rounded-2xl py-4 pr-12 pl-4 shadow-sm outline-none focus:ring-2 focus:ring-orange-500/20"
                                        value={searchQuery}
                                        onChange={(e) => setSearchQuery(e.target.value)}
                                    />
                                    <div className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400">
                                        <i data-lucide="search" className="w-5 h-5"></i>
                                    </div>
                                </div>

                                <div className="space-y-5">
                                    {filteredLectures.map(lecture => (
                                        <div key={lecture.id} className="bg-white rounded-[2rem] p-5 shadow-sm border border-gray-50 relative overflow-hidden group">
                                            <div className="w-10 h-10 bg-orange-500 text-white rounded-xl flex items-center justify-center font-bold absolute left-0 top-0 rounded-tr-none rounded-bl-2xl shadow-lg">
                                                {lecture.id}
                                            </div>
                                            <div className="mb-6 mt-2">
                                                <h3 className="font-bold text-lg text-gray-800 leading-tight mb-1">{lecture.title}</h3>
                                                <p className="text-sm text-gray-400">د. {lecture.doctor.replace('د. ', '')}</p>
                                            </div>

                                            <div className="grid grid-cols-4 gap-3">
                                                <ActionButton icon="book-open" label="الملزمة" color="bg-blue-500" link={lecture.material} />
                                                <ActionButton icon="mic" label="التسجيل" color="bg-orange-500" link={lecture.recording} />
                                                <ActionButton icon="file-text" label="التقرير" color="bg-yellow-500" link={lecture.report} />
                                                <ActionButton icon="users" label="التفريغات" color="bg-green-500" link={lecture.material} />
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </motion.div>
                        )}
                    </AnimatePresence>

                    {view !== 'splash' && (
                        <nav className="fixed bottom-0 left-0 right-0 max-w-md mx-auto bg-white/80 backdrop-blur-xl border-t border-gray-100 px-8 py-4 flex justify-between items-center z-50">
                            <NavButton active={view === 'index'} icon="layout-grid" label="الرئيسية" onClick={() => setView('index')} />
                            <NavButton active={false} icon="search" label="البحث" onClick={() => setView('index')} />
                            <NavButton active={false} icon="user" label="البروفايل" onClick={() => {}} />
                        </nav>
                    )}
                </div>
            );
        }

        function ActionButton({ icon, label, color, link }) {
            return (
                <a href={link} target="_blank" className="flex flex-col items-center gap-2 group">
                    <div className={`w-12 h-12 ${color} rounded-xl flex items-center justify-center text-white shadow-lg group-active:scale-90 transition-transform`}>
                        <i data-lucide={icon} className="w-6 h-6"></i>
                    </div>
                    <span className="text-[10px] font-bold text-gray-600">{label}</span>
                </a>
            );
        }

        function NavButton({ active, icon, label, onClick }) {
            return (
                <button onClick={onClick} className={`flex flex-col items-center gap-1 ${active ? 'text-orange-500' : 'text-gray-400'}`}>
                    <i data-lucide={icon} className="w-6 h-6"></i>
                    <span className="text-[10px] font-bold">{label}</span>
                </button>
            );
        }

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
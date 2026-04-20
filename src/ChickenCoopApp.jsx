import { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';

export default function ChickenCoopApp() {
  const { t, i18n } = useTranslation();
  const [currentDate, setCurrentDate] = useState(new Date());
  const [assignments, setAssignments] = useState(() => {
    const saved = localStorage.getItem('assignments');
    return saved ? JSON.parse(saved) : {};
  });
  const [showModal, setShowModal] = useState(false);
  const [selectedSlot, setSelectedSlot] = useState(null);
  const [inputName, setInputName] = useState('');
  useEffect(() => {
    localStorage.setItem('assignments', JSON.stringify(assignments));
  }, [assignments]);

  const goToPreviousMonth = () => {
    const newDate = new Date(currentDate);
    newDate.setMonth(newDate.getMonth() - 1);
    setCurrentDate(newDate);
  };

  const goToNextMonth = () => {
    const newDate = new Date(currentDate);
    newDate.setMonth(newDate.getMonth() + 1);
    setCurrentDate(newDate);
  };

  const monthYear = currentDate.toLocaleDateString(i18n.language, { 
    month: 'long', 
    year: 'numeric' 
  });

  const getDaysInMonth = () => {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const daysInMonth = lastDay.getDate();
    const startingDayOfWeek = firstDay.getDay();
    
    const days = [];
    
    for (let i = 0; i < startingDayOfWeek; i++) {
      days.push(null);
    }
    
    for (let day = 1; day <= daysInMonth; day++) {
      days.push(day);
    }
    
    return days;
  };

  const getDayOfWeek = (day) => {
    // Returns day of week from numerical date
    const date = new Date(currentDate.getFullYear(), currentDate.getMonth(), day);
    return date.toLocaleDateString(i18n.language, { weekday: 'short' });
  }
  const getDaysOfWeek = () => {
    // Returns list of abbreviated days of week starting from Sunday in the current language 
    const days = [];
    for (let i = 0; i < 7; i++) {
        const date = new Date(2024, 0, i); // Jan 2024 starts on Monday, i=0 is Sunday
        days.push(date.toLocaleDateString(i18n.language, { weekday: 'short' }));
      }
      return days;
  };

  const weekDays = getDaysOfWeek();

  const daysArray = getDaysInMonth();

  const getAssignmentKey = (day, slotType) => {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    return `${year}-${month}-${day}-${slotType}`;
  };

  const getAssignment = (day, slotType) => {
    const key = getAssignmentKey(day, slotType);
    return assignments[key] || null;
  };

  const handleSlotClick = (day, slotType) => {
    const currentAssignment = getAssignment(day, slotType);
    setSelectedSlot({ day, slotType });
    setInputName(currentAssignment || '');
    setShowModal(true);
  };

  const handleSave = () => {
    if (selectedSlot) {
      const key = getAssignmentKey(selectedSlot.day, selectedSlot.slotType);
      const newAssignments = { ...assignments };
      
      if (inputName.trim() === '') {
        delete newAssignments[key];
      } else {
        newAssignments[key] = inputName.trim();
      }
      
      setAssignments(newAssignments);
    }
    setShowModal(false);
    setInputName('');
    setSelectedSlot(null);
  };

  const handleCancel = () => {
    setShowModal(false);
    setInputName('');
    setSelectedSlot(null);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-4xl mx-auto">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-3xl font-bold text-gray-800">
            🐔 {t('chicken_coop_manager')}
          </h1>
          <button onClick={() => i18n.changeLanguage(i18n.language === 'fr' ? 'en' : 'fr')}>
            {i18n.language === 'fr' ? '🇬🇧 EN' : '🇫🇷 FR'}
          </button>
        </div>

        
        
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between mb-6">
            <button 
              onClick={goToPreviousMonth}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
              ← {t('previous')}
            </button>
            <h2 className="text-2xl font-semibold">
              {monthYear}
            </h2>
            <button 
              onClick={goToNextMonth}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
               {t('next')} →
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-7 gap-2">
            {weekDays.map(day => (
              <div key={day} className="text-center font-semibold text-gray-600 py-2 hidden md:block">
                {day}
              </div>
            ))}
            
            {daysArray.map((day, index) => (
              <div 
                key={index}
                className={`border rounded p-2 min-h-32 bg-gray-50 ${day ? '' : 'hidden md:block'}`}
              >
                {day && (
                  <div>
                    <div className="flex items-center gap-1 mb-2 font-semibold text-gray-800">
                      <span className="md:hidden">{getDayOfWeek(day)}</span>
                      <span>{day}</span>
                    </div>

                    <div className="text-xs mb-1">
                      <div className="font-medium text-gray-600">🌅  {t('day')}:</div>
                      <div 
                        onClick={() => handleSlotClick(day, 'day')}
                        className="bg-white border rounded px-2 py-1 text-gray-800 cursor-pointer hover:bg-blue-50"
                      >
                        {getAssignment(day, 'day') || t('empty')}
                      </div>
                    </div>
                    
                    <div className="text-xs">
                      <div className="font-medium text-gray-600">🌙  {t('evening')}:</div>
                      <div 
                        onClick={() => handleSlotClick(day, 'evening')}
                        className="bg-white border rounded px-2 py-1 text-gray-800 cursor-pointer hover:bg-blue-50"
                      >
                        {getAssignment(day, 'evening') || t('empty')}
                      </div>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>

        {showModal && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
            <div className="bg-white rounded-lg p-6 max-w-sm w-full mx-4">
              <h3 className="text-lg font-semibold mb-4">
                {t('assign_slot')}
              </h3>
              <p className="text-sm text-gray-600 mb-4">
                {selectedSlot && `${currentDate.toLocaleDateString(i18n.language, { month: 'long' })} ${selectedSlot.day} - ${selectedSlot.slotType === 'day' ? '🌅 Day' : '🌙 Evening'}`}
              </p>
              <input
                type="text"
                value={inputName}
                onChange={(e) => setInputName(e.target.value)}
                placeholder="Enter your name"
                className="w-full border rounded px-3 py-2 mb-4"
                autoFocus
              />
              <div className="flex gap-2">
                <button
                  onClick={handleCancel}
                  className="flex-1 px-4 py-2 bg-gray-300 rounded hover:bg-gray-400"
                >
                  {t('cancel')}
                </button>
                <button
                  onClick={handleSave}
                  className="flex-1 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
                >
                  {t('save')}
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
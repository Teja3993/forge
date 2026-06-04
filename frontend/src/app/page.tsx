import React from 'react';

const HomePage = () => {
  return (
    // The outermost container: Full screen height, Flex row (side by side), dark background
    <div className="flex h-screen w-full bg-gray-900 text-gray-100 font-sans">
      
      {/* 1. SIDEBAR AREA */}
      {/* w-64 is a fixed width (16rem/256px). flex-shrink-0 ensures it never squishes. */}
      <div className="w-[256px] min-w-[256px] max-w-[256px] flex-none bg-gray-800 border-r border-gray-700 flex flex-col">
        {/* Sidebar Header */}
        <div className="p-4 border-b border-gray-700">
          <h1 className="text-xl font-bold text-blue-400">Forge Workspace</h1>
        </div>
        
        {/* Sidebar List (Static for now) */}
        <div className="flex-1 overflow-y-auto p-4 space-y-2">
          <p className="text-xs text-gray-400 uppercase font-semibold tracking-wider mb-2">History</p>
          
          {/* Dummy Snippet Items */}
          <div className="p-2 rounded bg-gray-700 hover:bg-gray-600 cursor-pointer transition-colors">
            <h3 className="text-sm font-medium">Hello World C++</h3>
            <p className="text-xs text-gray-400">cpp • 2 hours ago</p>
          </div>
          <div className="p-2 rounded hover:bg-gray-700 cursor-pointer transition-colors">
            <h3 className="text-sm font-medium">Binary Search Tree</h3>
            <p className="text-xs text-gray-400">cpp • Yesterday</p>
          </div>
        </div>
      </div>

      {/* 2. MAIN WORKSPACE AREA */}
      {/* flex-1 takes up all remaining width. flex flex-col stacks items vertically. */}
      <div className="flex-1 flex flex-col h-full overflow-hidden">
        
        {/* Top Navbar / Action Bar */}
        <div className="h-16 flex items-center justify-between px-6 bg-gray-900 border-b border-gray-800">
          <div className="flex items-center space-x-4">
             {/* We'll add language selectors or titles here later */}
             <span className="text-sm text-gray-400">Language: C++</span>
          </div>
          
          {/* The Run Button */}
          <button className="px-6 py-2 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded shadow-lg transition-all focus:outline-none focus:ring-2 focus:ring-blue-400">
            Run Code
          </button>
        </div>

        {/* Text Area Container */}
        <div className="flex-1 p-6 bg-[#1e1e1e]"> 
          {/* #1e1e1e is the classic VS Code background color! */}
          <textarea 
            className="w-full h-full bg-transparent text-gray-300 font-mono text-sm resize-none focus:outline-none"
            placeholder="// Write your C++ code here..."
            spellCheck="false"
          ></textarea>
        </div>

      </div>
    </div>
  );
};

export default HomePage;
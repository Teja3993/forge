// This directive tells Next.js this component needs browser interactivity
"use client";
import React, { useState } from 'react';

const HomePage = () => {
  // 2. Define the State: 'code' holds the text, 'setCode' is the function to update it.
  const [code, setCode] = useState("");

  // 3. Define the Click Handler
  const handleRunClick = () => {
    console.log("Current Code State:", code);
    alert("Check your browser console! State captured.");
  };
  return (
    <div className="flex h-screen w-full bg-gray-900 text-gray-100 font-sans">
      
      {/* SIDEBAR AREA (Unchanged) */}
      <div className="w-64 flex-shrink-0 bg-gray-800 border-r border-gray-700 flex flex-col">
        <div className="p-4 border-b border-gray-700">
          <h1 className="text-xl font-bold text-blue-400">Forge Workspace</h1>
        </div>
        <div className="flex-1 overflow-y-auto p-4 space-y-2">
          <p className="text-xs text-gray-400 uppercase font-semibold tracking-wider mb-2">History</p>
          <div className="p-2 rounded bg-gray-700 hover:bg-gray-600 cursor-pointer transition-colors">
            <h3 className="text-sm font-medium">Hello World C++</h3>
            <p className="text-xs text-gray-400">cpp • 2 hours ago</p>
          </div>
        </div>
      </div>

      {/* MAIN WORKSPACE AREA */}
      <div className="flex-1 flex flex-col h-full overflow-hidden">
        
        {/* Top Navbar */}
        <div className="h-16 flex items-center justify-between px-6 bg-gray-900 border-b border-gray-800">
          <div className="flex items-center space-x-4">
             <span className="text-sm text-gray-400">Language: C++</span>
          </div>
          
          {/* 4. Bind the onClick event to our handler */}
          <button 
            onClick={handleRunClick}
            className="px-6 py-2 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded shadow-lg transition-all focus:outline-none focus:ring-2 focus:ring-blue-400"
          >
            Run Code
          </button>
        </div>

        {/* Text Area Container */}
        <div className="flex-1 p-6 bg-[#1e1e1e]"> 
          {/* 5. The Controlled Component: Value is locked to state, onChange updates state */}
          <textarea 
            value={code}
            onChange={(e) => setCode(e.target.value)}
            className="w-full h-full bg-transparent text-gray-300 font-mono text-sm resize-none focus:outline-none"
            placeholder="// Write your C++ code here..."
            spellCheck="false"
          />
        </div>
      </div>
    </div>
  );
};

export default HomePage;
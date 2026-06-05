// This directive tells Next.js this component needs browser interactivity
"use client";
import React, { useState, useEffect } from 'react';

// 1. Define the TypeScript interface for the data (matches SnippetResponse from Pydantic)
interface Snippet{
  id: string;
  title: string;
  language: string;
  code: string;
  created_at: string
}
const HomePage = () => {
  // Define the State: 'code' holds the text, 'setCode' is the function to update it.
  const [code, setCode] = useState("");
  // State to track if currently loading(to disable the button)
  const [isExecuting, setIsExecuting] = useState(false);

  // State to hold array of snippetsconst
  const [history, setHistory] = useState<Snippet[]>([]);

  // The Fetch function (extracted to reuse it)
  const fetchHistory = async () => {
    try{
      const response = await fetch('http://localhost:8000/snippets/');
      if (!response.ok) throw new Error("Failed to fetch history");
      const data = await response.json();
      setHistory(data);
    } catch (error){
      console.error("Error fetching history: ", error);
    }
  };
  // The useEffect Hook
  // The empty array [] means "Run this once on mount"
  useEffect(() => {
    fetchHistory();
  }, []);



  // Marking the function as async
  const handleRunClick = async () => {
    // Preventing empty submission
    if( !code.trim()) return;

    setIsExecuting(true); // locking the button

    try{
      // 2. The Fetch API
      const response = await fetch('http://localhost:8000/snippets/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        //  Serialize the payload. 
        
        body: JSON.stringify({
          title: `Snippet ${new Date().toLocaleTimeString()}`, // Dynamic title
          language: "cpp",
          code: code,
          user_id: "8db81971-dcae-40ef-9e04-77f5c5547c2d" 
        })
      });

      // 4. Trap check: fetch() only throws errors if the network physically fails.
      // We must manually check if the backend returned a 400/500 error.
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Refreshing the history so the sidebar updates immediately
      await fetchHistory();

      // 5. Await the JSON parsing of the response body
      const data = await response.json();
      
      // 6. Log the success!
      // console.log("Success! Backend saved snippet:", data);
      // alert("Snippet successfully saved to Postgres!");

    } catch (error) {
      console.error("Failed to execute code:", error);
      alert("Network or Server Error. Check console.");
    } finally {
      setIsExecuting(false); // Unlock the button, even if it failed
    }
    
  };
  return (
    <div className="flex h-screen w-full bg-gray-900 text-gray-100 font-sans">
      
      {/* SIDEBAR AREA */}
      <div className="w-64 flex-shrink-0 bg-gray-800 border-r border-gray-700 flex flex-col">
        <div className="p-4 border-b border-gray-700">
          <h1 className="text-xl font-bold text-blue-400">Forge Workspace</h1>
        </div>
        <div className="flex-1 overflow-y-auto p-4 space-y-2">
          <p className="text-xs text-gray-400 uppercase font-semibold tracking-wider mb-2">History</p>
          {/* 6. NEW: Dynamic Rendering using .map() */}
          {history.length === 0 ? (
            <p className="text-sm text-gray-500 italic">No snippets yet.</p>
          ) : (
            history.map((snippet) => (
              // CRITICAL: The 'key' prop is required by React to track list items
              <div key={snippet.id} className="p-2 rounded bg-gray-700 hover:bg-gray-600 cursor-pointer transition-colors mb-2">
                <h3 className="text-sm font-medium truncate">{snippet.title}</h3>
                <p className="text-xs text-gray-400">{new Date(snippet.created_at).toLocaleDateString()}</p>
              </div>
            ))
          )}
        </div>
      </div>

      {/* MAIN WORKSPACE AREA */}
      <div className="flex-1 flex flex-col h-full overflow-hidden">
        
        {/* Top Navbar */}
        <div className="h-16 flex items-center justify-between px-6 bg-gray-900 border-b border-gray-800">
          <div className="flex items-center space-x-4">
             <span className="text-sm text-gray-400">Language: C++</span>
          </div>
          
          {/* Disable the button while it is executing */}
          <button 
            onClick={handleRunClick}
            disabled = {isExecuting}
            className={`px-6 py-2 font-bold rounded shadow-lg transition-all focus:outline-none focus:ring-2 focus:ring-blue-400
              ${isExecuting ? 'bg-gray-600 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-500 text-white'}`}
          >
            {isExecuting ? 'Executing...' : 'Run Code'}
          </button>
        </div>

        {/* Text Area Container */}
        <div className="flex-1 p-6 bg-[#1e1e1e]"> 
          {/* The Controlled Component: Value is locked to state, onChange updates state */}
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
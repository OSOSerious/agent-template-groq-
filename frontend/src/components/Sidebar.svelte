<!-- Sidebar.svelte -->
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { chatStore, type ChatSession } from '../stores/chatStore';

  const dispatch = createEventDispatcher();
  let activeView = 'templates';
  let chatSessions: ChatSession[] = [];

  chatStore.subscribe(value => {
    chatSessions = value;
  });

  const navItems = [
    { id: 'home', label: '🏠 Home', view: 'home' },
    { id: 'templates', label: '📋 Templates', view: 'templates' },
    { id: 'chats', label: '💬 Chat History', view: 'chats' },
    { id: 'newagent', label: '🤖 New Agent', view: 'newagent' },
    { id: 'settings', label: '⚙️ Settings', view: 'settings' }
  ];

  function handleNavClick(view: string) {
    activeView = view;
    dispatch('viewChange', { view });
  }
</script>

<div class="flex flex-col h-full bg-gray-900 text-white w-64 p-4">
  <div class="flex items-center justify-between mb-8">
    <h1 class="text-xl font-bold">AgentGPT</h1>
  </div>

  <nav class="flex-1">
    <ul class="space-y-2">
      {#each navItems as item}
        <li>
          <button
            class="w-full px-4 py-2 text-left rounded-lg transition-colors duration-200
                   {activeView === item.view ? 'bg-blue-600' : 'hover:bg-gray-800'}"
            on:click={() => handleNavClick(item.view)}
          >
            {item.label}
          </button>
        </li>
      {/each}
    </ul>

    {#if activeView === 'chats'}
      <div class="mt-6">
        <h2 class="text-sm font-semibold text-gray-400 mb-2">Recent Chats</h2>
        <ul class="space-y-1">
          {#each chatSessions as session}
            <li>
              <button
                class="w-full px-4 py-2 text-left text-sm rounded-lg hover:bg-gray-800 truncate"
                title={session.agentName}
              >
                {session.agentName}
              </button>
            </li>
          {/each}
        </ul>
      </div>
    {/if}
  </nav>

  <div class="mt-auto pt-4 border-t border-gray-800">
    <div class="text-sm text-gray-400">
      <p>Powered by Groq API</p>
    </div>
  </div>
</div>

<style>
  :global(body) {
    background-color: #111827;
    color: white;
  }
</style>

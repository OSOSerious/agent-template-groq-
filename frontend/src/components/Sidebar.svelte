<!-- Sidebar.svelte -->
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  export let activeView: string = 'home';

  const menuItems = [
    { id: 'home', label: 'Home', icon: '🏠' },
    { id: 'templates', label: 'Templates', icon: '📄' },
    { id: 'my-agents', label: 'My Agents', icon: '🤖' },
    { id: 'help', label: 'Help', icon: '❓' },
    { id: 'settings', label: 'Settings', icon: '⚙️' }
  ];

  function handleNavigate(view: string) {
    activeView = view;
    dispatch('navigate', { view });
  }

  function handleNewAgent() {
    dispatch('newAgent');
  }
</script>

<aside class="fixed left-0 top-0 h-screen w-64 bg-[#1a1b26] text-white border-r border-gray-800">
  <div class="p-4">
    <div class="flex items-center space-x-2 mb-8">
      <h1 class="text-xl font-bold">Agent Console</h1>
      <span class="px-2 py-1 text-xs bg-blue-600 rounded-full">beta</span>
    </div>
    <p class="text-sm text-gray-400 mb-6">Create & manage your AI agents</p>
  </div>

  <nav class="space-y-1">
    {#each menuItems as item}
      <button
        class="w-full px-4 py-2 text-left hover:bg-gray-800 flex items-center space-x-3 {activeView === item.id ? 'bg-gray-800' : ''}"
        on:click={() => handleNavigate(item.id)}
      >
        <span class="text-lg">{item.icon}</span>
        <span>{item.label}</span>
      </button>
    {/each}

    <button
      class="w-full px-4 py-2 mt-4 bg-blue-600 hover:bg-blue-700 text-white rounded-lg flex items-center justify-center space-x-2"
      on:click={handleNewAgent}
    >
      <span>+</span>
      <span>New Agent</span>
    </button>
  </nav>

  <div class="absolute bottom-0 left-0 w-full p-4">
    <button
      class="w-full px-4 py-2 bg-orange-500 hover:bg-orange-600 text-white rounded-lg flex items-center justify-center space-x-2"
    >
      <span>⭐</span>
      <span>Subscribe</span>
    </button>
  </div>
</aside>

<style>
  :global(body) {
    background-color: #111827;
    color: white;
  }
</style>

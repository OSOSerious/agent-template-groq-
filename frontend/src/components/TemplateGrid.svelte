<!-- TemplateGrid.svelte -->
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { Template } from '../types';

  export let templates: Template[] = [];
  const dispatch = createEventDispatcher();

  function handleTemplateClick(template: Template) {
    dispatch('select', template);
  }
</script>

<div class="p-4">
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    {#each templates as template}
      <button
        class="flex items-start space-x-4 p-4 bg-gray-800/50 backdrop-blur-sm border border-gray-700/50 rounded-lg hover:bg-gray-700/50 transition-colors"
        on:click={() => handleTemplateClick(template)}
      >
        <div class="w-12 h-12 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-2xl">
          {template.icon || '🤖'}
        </div>
        <div class="flex-1 text-left">
          <h3 class="text-lg font-semibold text-white">{template.name}</h3>
          <p class="text-sm text-gray-400">{template.description}</p>
        </div>
      </button>
    {/each}
  </div>

  {#if templates.length === 0}
    <div class="text-center text-gray-400 mt-8">
      Loading templates...
    </div>
  {/if}
</div>

<style>
  /* All styles are handled by Tailwind classes */
</style>

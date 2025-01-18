<!-- TemplateGrid.svelte -->
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { Template } from '../types';

  const dispatch = createEventDispatcher();

  export let templates: Template[] = [];
  let searchQuery = '';

  $: filteredTemplates = templates.filter(template =>
    template.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    template.description.toLowerCase().includes(searchQuery.toLowerCase())
  );

  function handleTemplateClick(template: Template) {
    dispatch('select', { template });
  }
</script>

<div class="p-4">
  <div class="mb-4">
    <input
      type="text"
      placeholder="Search templates..."
      bind:value={searchQuery}
      class="w-full p-2 rounded bg-gray-800 border border-gray-700 text-white placeholder-gray-400"
    />
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    {#each filteredTemplates as template}
      <button
        class="p-4 rounded-lg bg-gray-800 hover:bg-gray-700 transition-colors text-left border border-gray-700"
        on:click={() => handleTemplateClick(template)}
      >
        <div class="flex items-start space-x-3">
          <div class="text-2xl">{template.icon}</div>
          <div class="flex-1">
            <h3 class="font-semibold text-white">
              {template.name}
            </h3>
            <p class="text-sm text-gray-400">
              {template.description}
            </p>
          </div>
        </div>
      </button>
    {/each}
  </div>

  {#if filteredTemplates.length === 0}
    <div class="text-center text-gray-400 mt-8">
      {#if templates.length === 0}
        Loading templates...
      {:else}
        No templates found matching "{searchQuery}"
      {/if}
    </div>
  {/if}
</div>

<style>
  :global(body) {
    @apply bg-gray-900;
  }
</style>

<script lang="ts">
  import { authStore } from '../stores/authStore';
  import { onMount } from 'svelte';

  let isLogin = true;
  let email = '';
  let username = '';
  let password = '';
  let error = '';
  let loading = false;

  async function handleSubmit() {
    loading = true;
    error = '';

    try {
      if (isLogin) {
        const success = await authStore.login(email, password);
        if (!success) {
          error = 'Invalid email or password';
        }
      } else {
        const success = await authStore.register(email, username, password);
        if (!success) {
          error = 'Registration failed. Please try again.';
        } else {
          // Auto-login after successful registration
          await authStore.login(email, password);
        }
      }
    } catch (e) {
      error = 'An error occurred. Please try again.';
    }

    loading = false;
  }
</script>

<div class="min-h-screen flex items-center justify-center bg-gray-900">
  <div class="max-w-md w-full space-y-8 p-8 bg-gray-800/50 backdrop-blur-sm rounded-xl border border-gray-700/50">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-white">
        {isLogin ? 'Sign in to your account' : 'Create your account'}
      </h2>
    </div>
    <form class="mt-8 space-y-6" on:submit|preventDefault={handleSubmit}>
      <div class="rounded-md shadow-sm space-y-4">
        <div>
          <label for="email" class="sr-only">Email address</label>
          <input
            id="email"
            name="email"
            type="email"
            required
            bind:value={email}
            class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-700 bg-gray-900/50 placeholder-gray-400 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            placeholder="Email address"
          />
        </div>
        {#if !isLogin}
          <div>
            <label for="username" class="sr-only">Username</label>
            <input
              id="username"
              name="username"
              type="text"
              required
              bind:value={username}
              class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-700 bg-gray-900/50 placeholder-gray-400 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="Username"
            />
          </div>
        {/if}
        <div>
          <label for="password" class="sr-only">Password</label>
          <input
            id="password"
            name="password"
            type="password"
            required
            bind:value={password}
            class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-700 bg-gray-900/50 placeholder-gray-400 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            placeholder="Password"
          />
        </div>
      </div>

      {#if error}
        <div class="text-red-500 text-sm text-center">{error}</div>
      {/if}

      <div>
        <button
          type="submit"
          disabled={loading}
          class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50"
        >
          {#if loading}
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </span>
          {/if}
          {loading ? 'Processing...' : (isLogin ? 'Sign in' : 'Register')}
        </button>
      </div>
    </form>

    <div class="text-center">
      <button
        on:click={() => isLogin = !isLogin}
        class="text-sm text-blue-400 hover:text-blue-300"
      >
        {isLogin ? "Don't have an account? Register" : 'Already have an account? Sign in'}
      </button>
    </div>
  </div>
</div>

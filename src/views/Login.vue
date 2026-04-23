<template>
  <div class="min-h-screen bg-gradient-to-br from-rose-400 via-fuchsia-500 to-purple-600 flex flex-col">
    <div class="flex-1 flex flex-col items-center justify-center px-8 pt-12">
      <div class="w-24 h-24 rounded-2xl bg-white/20 backdrop-blur-sm flex items-center justify-center mb-6 shadow-2xl">
        <span class="text-5xl">🛍️</span>
      </div>
      <h1 class="text-white text-3xl font-bold mb-3">时尚商城</h1>
      <p class="text-white/80 text-base">精选服饰 品质生活</p>
      
      <div class="flex gap-4 mt-8">
        <div class="w-10 h-10 rounded-full bg-white/20 backdrop-blur-sm flex items-center justify-center">
          <span class="text-xl">👕</span>
        </div>
        <div class="w-10 h-10 rounded-full bg-white/20 backdrop-blur-sm flex items-center justify-center">
          <span class="text-xl">👟</span>
        </div>
        <div class="w-10 h-10 rounded-full bg-white/20 backdrop-blur-sm flex items-center justify-center">
          <span class="text-xl">💍</span>
        </div>
        <div class="w-10 h-10 rounded-full bg-white/20 backdrop-blur-sm flex items-center justify-center">
          <span class="text-xl">👜</span>
        </div>
      </div>
    </div>

    <div class="bg-white rounded-t-[2.5rem] p-8 pb-12 shadow-2xl">
      <div class="mb-6 text-center">
        <h2 class="text-xl font-bold text-gray-800">欢迎登录</h2>
        <p class="text-sm text-gray-500 mt-1">登录后享受更多优惠</p>
      </div>

      <div class="space-y-5">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">用户名</label>
          <div class="relative">
            <span class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400">👤</span>
            <input 
              v-model="form.name"
              type="text" 
              placeholder="请输入用户名"
              class="w-full h-12 pl-12 pr-4 bg-gray-50 border border-gray-100 rounded-xl text-sm focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-100 transition-all"
            />
          </div>
        </div>
        
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">密码</label>
          <div class="relative">
            <span class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400">🔒</span>
            <input 
              v-model="form.password"
              type="password" 
              placeholder="请输入密码"
              class="w-full h-12 pl-12 pr-4 bg-gray-50 border border-gray-100 rounded-xl text-sm focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-100 transition-all"
            />
          </div>
        </div>

        <div class="flex items-center justify-between text-sm">
          <label class="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" class="w-4 h-4 text-purple-500 rounded focus:ring-purple-500" />
            <span class="text-gray-500">记住我</span>
          </label>
          <span class="text-purple-500 cursor-pointer hover:underline">忘记密码?</span>
        </div>

        <button 
          class="w-full h-12 rounded-xl bg-gradient-to-r from-purple-500 to-fuchsia-500 text-white font-semibold mt-2 shadow-lg shadow-purple-500/30 hover:shadow-purple-500/50 transition-all hover:scale-[1.02] active:scale-[0.98]"
          :disabled="!isFormValid"
          :class="!isFormValid ? 'opacity-50' : ''"
          @click="handleLogin"
        >
          立即登录
        </button>

        <div class="flex items-center gap-4 my-4">
          <div class="flex-1 h-px bg-gray-200"></div>
          <span class="text-xs text-gray-400">或</span>
          <div class="flex-1 h-px bg-gray-200"></div>
        </div>

        <button 
          class="w-full h-12 rounded-xl border-2 border-gray-200 text-gray-600 font-semibold hover:border-purple-300 hover:bg-purple-50 transition-all"
          @click="handleGuestLogin"
        >
          游客进入
        </button>
      </div>

      <p class="text-center text-xs text-gray-400 mt-6">
        登录即表示同意我们的
        <span class="text-purple-500 cursor-pointer">服务条款</span>
        和
        <span class="text-purple-500 cursor-pointer">隐私政策</span>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '../stores/user'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const form = ref({
  name: 'user',
  password: '123456'
})

const isFormValid = computed(() => {
  return form.value.name && form.value.password
})

const handleLogin = () => {
  if (!isFormValid.value) return
  
  userStore.login({
    name: form.value.name
  })
  
  const redirect = route.query.redirect || '/'
  router.replace(redirect)
}

const handleGuestLogin = () => {
  userStore.loginAsGuest()
  const redirect = route.query.redirect || '/'
  router.replace(redirect)
}
</script>

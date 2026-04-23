<template>
  <div class="min-h-screen bg-gray-100">
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
    <nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 z-40 safe-area-bottom">
      <div class="flex justify-around items-center h-14">
        <router-link 
          v-for="item in navItems" 
          :key="item.path"
          :to="item.path"
          class="flex flex-col items-center justify-center flex-1 h-full"
          :class="[
            $route.path === item.path ? 'text-primary' : 'text-gray-500'
          ]"
        >
          <component :is="item.icon" class="w-6 h-6" />
          <span class="text-xs mt-1">{{ item.label }}</span>
        </router-link>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { h } from 'vue'
import { useCartStore } from './stores/cart'

const cartStore = useCartStore()

const HomeIcon = {
  render: () => h('svg', {
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'none',
    viewBox: '0 0 24 24',
    strokeWidth: 1.5,
    stroke: 'currentColor'
  }, [
    h('path', {
      strokeLinecap: 'round',
      strokeLinejoin: 'round',
      d: 'M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25'
    })
  ])
}

const CategoryIcon = {
  render: () => h('svg', {
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'none',
    viewBox: '0 0 24 24',
    strokeWidth: 1.5,
    stroke: 'currentColor'
  }, [
    h('path', {
      strokeLinecap: 'round',
      strokeLinejoin: 'round',
      d: 'M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5'
    })
  ])
}

const CartIcon = {
  render: () => h('svg', {
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'none',
    viewBox: '0 0 24 24',
    strokeWidth: 1.5,
    stroke: 'currentColor'
  }, [
    h('path', {
      strokeLinecap: 'round',
      strokeLinejoin: 'round',
      d: 'M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 00-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 00-16.536-1.84M7.5 14.25L5.106 5.272M6 20.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm12.75 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0z'
    })
  ])
}

const ProfileIcon = {
  render: () => h('svg', {
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'none',
    viewBox: '0 0 24 24',
    strokeWidth: 1.5,
    stroke: 'currentColor'
  }, [
    h('path', {
      strokeLinecap: 'round',
      strokeLinejoin: 'round',
      d: 'M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z'
    })
  ])
}

const navItems = [
  { path: '/', label: '首页', icon: HomeIcon },
  { path: '/category', label: '分类', icon: CategoryIcon },
  { path: '/cart', label: '购物车', icon: CartIcon, badge: () => cartStore.totalItems },
  { path: '/profile', label: '我的', icon: ProfileIcon }
]
</script>

<style scoped>
.safe-area-bottom {
  padding-bottom: env(safe-area-inset-bottom);
}
</style>

<template>
  <div class="min-h-screen bg-gray-50">
    <!-- 顶部导航 -->
    <div class="bg-primary px-4 py-3">
      <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <h1 class="text-white text-lg font-bold">关于我们</h1>
      </div>
    </div>

    <!-- 内容区域 -->
    <div class="p-4 space-y-6">
      <!-- Logo 区域 -->
      <div class="flex flex-col items-center py-6">
        <div class="w-20 h-20 rounded-full bg-gradient-to-br from-pink-400 to-purple-500 flex items-center justify-center shadow-lg mb-4">
          <span class="text-white text-3xl">👗</span>
        </div>
        <h2 class="text-xl font-bold text-gray-800">时尚商城</h2>
        <p class="text-sm text-gray-500 mt-1">专注服饰穿搭 品质生活之选</p>
      </div>

      <!-- 平台介绍 -->
      <div class="bg-white rounded-lg shadow-sm p-5 space-y-4">
        <h3 class="text-lg font-bold text-gray-800 flex items-center gap-2">
          <span class="w-1 h-5 bg-primary rounded-full"></span>
          平台简介
        </h3>
        <p class="text-sm text-gray-600 leading-relaxed text-justify">
          本时尚商城是专注于服饰穿搭领域的线上综合购物平台，平台商品覆盖服装、鞋类、箱包、首饰配饰等全时尚品类，构建完整的日常穿搭商品体系。
        </p>
      </div>

      <!-- 经营理念 -->
      <div class="bg-white rounded-lg shadow-sm p-5 space-y-4">
        <h3 class="text-lg font-bold text-gray-800 flex items-center gap-2">
          <span class="w-1 h-5 bg-primary rounded-full"></span>
          经营理念
        </h3>
        <div class="flex justify-center gap-8 py-2">
          <div class="flex flex-col items-center">
            <div class="w-14 h-14 rounded-full bg-pink-50 flex items-center justify-center mb-2">
              <span class="text-2xl">✨</span>
            </div>
            <span class="text-sm font-medium text-gray-700">品质为先</span>
          </div>
          <div class="flex flex-col items-center">
            <div class="w-14 h-14 rounded-full bg-purple-50 flex items-center justify-center mb-2">
              <span class="text-2xl">❤️</span>
            </div>
            <span class="text-sm font-medium text-gray-700">用户为本</span>
          </div>
        </div>
        <p class="text-sm text-gray-600 leading-relaxed text-justify">
          自平台创立以来，我们始终以"品质为先、用户为本"为经营理念，严格筛选供应链与商品质检标准，兼顾时尚设计、面料舒适度与产品性价比，满足广大用户多元化、全场景的日常穿搭需求。
        </p>
      </div>

      <!-- 平台特色 -->
      <div class="bg-white rounded-lg shadow-sm p-5 space-y-4">
        <h3 class="text-lg font-bold text-gray-800 flex items-center gap-2">
          <span class="w-1 h-5 bg-primary rounded-full"></span>
          平台特色
        </h3>
        <div class="grid grid-cols-2 gap-4">
          <div class="flex items-start gap-3 p-3 bg-gray-50 rounded-lg">
            <span class="text-xl">🎯</span>
            <div>
              <p class="text-sm font-medium text-gray-800">智能推荐</p>
              <p class="text-xs text-gray-500 mt-1">首页个性化商品推荐</p>
            </div>
          </div>
          <div class="flex items-start gap-3 p-3 bg-gray-50 rounded-lg">
            <span class="text-xl">📂</span>
            <div>
              <p class="text-sm font-medium text-gray-800">品类齐全</p>
              <p class="text-xs text-gray-500 mt-1">精细化品类导航</p>
            </div>
          </div>
          <div class="flex items-start gap-3 p-3 bg-gray-50 rounded-lg">
            <span class="text-xl">🔍</span>
            <div>
              <p class="text-sm font-medium text-gray-800">便捷搜索</p>
              <p class="text-xs text-gray-500 mt-1">快速检索心仪商品</p>
            </div>
          </div>
          <div class="flex items-start gap-3 p-3 bg-gray-50 rounded-lg">
            <span class="text-xl">🛒</span>
            <div>
              <p class="text-sm font-medium text-gray-800">一站购物</p>
              <p class="text-xs text-gray-500 mt-1">流畅购物流程</p>
            </div>
          </div>
          <div class="flex items-start gap-3 p-3 bg-gray-50 rounded-lg col-span-2">
            <span class="text-xl">🛡️</span>
            <div>
              <p class="text-sm font-medium text-gray-800">完善售后</p>
              <p class="text-xs text-gray-500 mt-1">全周期用户售后体系保障</p>
            </div>
          </div>
        </div>
        <p class="text-sm text-gray-600 leading-relaxed text-justify">
          平台搭载智能化首页推荐、精细化品类导航、便捷搜索检索、一站式购物流程及完善的用户售后体系，紧跟当下潮流穿搭趋势，持续更新款式品类，优化页面交互与购物功能，致力于为广大用户打造流畅、安心、高性价比的线上服饰购物体验。
        </p>
      </div>

      <!-- 未来展望 -->
      <div class="bg-white rounded-lg shadow-sm p-5 space-y-4">
        <h3 class="text-lg font-bold text-gray-800 flex items-center gap-2">
          <span class="w-1 h-5 bg-primary rounded-full"></span>
          未来展望
        </h3>
        <p class="text-sm text-gray-600 leading-relaxed text-justify">
          未来我们将不断升级商品供应链与服务能力，坚守品质初心，为用户提供更优质的穿搭好物与全周期购物服务。
        </p>
        <div class="flex justify-center py-4">
          <div class="text-center">
            <p class="text-primary font-medium">携手共进 · 时尚同行</p>
            <p class="text-xs text-gray-400 mt-1">感谢您选择时尚商城</p>
          </div>
        </div>
      </div>

      <!-- 版本信息 -->
      <div class="text-center py-4">
        <p class="text-xs text-gray-400">版本号: v1.0.0</p>
        <p class="text-xs text-gray-400 mt-1">© 2024 时尚商城 版权所有</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goBack = () => {
  router.back()
}
</script>

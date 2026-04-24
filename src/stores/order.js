import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { orderApi } from '@/api/order'

// 转换后端订单数据为前端格式
const transformOrderData = (data) => {
  if (!data) return null
  return {
    id: data.id,
    orderNo: data.order_no,
    status: data.status,
    totalPrice: data.total_amount,
    originalPrice: data.original_amount,
    discountAmount: data.discount_amount,
    isVIPOrder: data.vip_discount < 1,
    createTime: data.created_at,
    payTime: data.pay_time,
    shipTime: data.ship_time,
    completeTime: data.complete_time,
    address: data.address_snapshot,
    note: data.note,
    items: data.items?.map(item => ({
      id: item.product_id,
      name: item.product_name,
      cover: item.product_cover,
      size: item.size,
      quantity: item.quantity,
      price: item.unit_price
    })) || []
  }
}

export const useOrderStore = defineStore('order', () => {
  const orders = ref([])
  const currentOrder = ref(null)
  const loading = ref(false)

  // 根据状态获取订单
  const getOrdersByStatus = (status) => {
    if (!orders.value || !Array.isArray(orders.value)) return []
    if (status === 'all') return orders.value
    return orders.value.filter(order => order.status === status)
  }

  // 根据ID获取订单
  const getOrderById = (orderId) => {
    if (!orders.value || !Array.isArray(orders.value)) return null
    return orders.value.find(order => order.id === parseInt(orderId)) || null
  }

  // 获取订单列表
  const fetchOrders = async (params = {}) => {
    loading.value = true
    try {
      const data = await orderApi.getOrders(params)
      // 转换后端数据为前端格式
      orders.value = Array.isArray(data) ? data.map(transformOrderData) : []
      return orders.value
    } catch (error) {
      console.error('获取订单列表失败:', error)
      orders.value = []
      return []
    } finally {
      loading.value = false
    }
  }

  // 获取订单详情
  const fetchOrderDetail = async (orderId) => {
    loading.value = true
    try {
      const data = await orderApi.getOrderDetail(orderId)
      // 转换后端数据为前端格式
      currentOrder.value = transformOrderData(data)
      return currentOrder.value
    } catch (error) {
      console.error('获取订单详情失败:', error)
      return null
    } finally {
      loading.value = false
    }
  }

  // 创建订单
  const createOrder = async (data) => {
    const order = await orderApi.createOrder(data)
    return order
  }

  // 支付订单
  const payOrder = async (orderId, payMethod) => {
    const result = await orderApi.payOrder(orderId, payMethod)
    // 更新本地订单状态
    await fetchOrderDetail(orderId)
    return result
  }

  // 取消订单
  const cancelOrder = async (orderId) => {
    await orderApi.cancelOrder(orderId)
    await fetchOrders()
  }

  // 确认收货
  const confirmOrder = async (orderId) => {
    await orderApi.confirmOrder(orderId)
    await fetchOrderDetail(orderId)
  }

  return {
    orders,
    currentOrder,
    loading,
    getOrdersByStatus,
    getOrderById,
    fetchOrders,
    fetchOrderDetail,
    createOrder,
    payOrder,
    cancelOrder,
    confirmOrder
  }
})

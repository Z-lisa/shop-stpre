import api from './request'

export const authApi = {
  // 注册
  register(data) {
    return api.post('/auth/register', data)
  },

  // 登录
  login(data) {
    return api.post('/auth/login', data)
  },

  // 获取当前用户信息
  getCurrentUser() {
    return api.get('/auth/me')
  },

  // 更新用户信息
  updateProfile(data) {
    return api.put('/auth/me', data)
  },

  // 修改密码
  changePassword(oldPassword, newPassword) {
    return api.post('/auth/change-password', null, {
      params: { old_password: oldPassword, new_password: newPassword }
    })
  }
}

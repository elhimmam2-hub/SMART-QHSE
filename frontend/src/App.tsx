import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Layout, Menu, theme } from 'antd'
import { DashboardOutlined, UserOutlined } from '@ant-design/icons'
import './App.css'

const { Header, Sider, Content, Footer } = Layout

function App() {
  const [collapsed, setCollapsed] = React.useState(false)
  const { token: { colorBgContainer, borderRadiusLG } } = theme.useToken()

  return (
    <Router>
      <Layout style={{ minHeight: '100vh' }}>
        <Sider trigger={null} collapsible collapsed={collapsed}>
          <div className="logo" style={{
            height: 64,
            margin: 16,
            background: 'rgba(255, 255, 255, 0.2)',
            borderRadius: borderRadiusLG,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'white',
            fontSize: 16,
            fontWeight: 'bold'
          }}>
            SMART QHSE
          </div>
          <Menu
            theme="dark"
            mode="inline"
            defaultSelectedKeys={['1']}
            items={[
              {
                key: '1',
                icon: <DashboardOutlined />,
                label: 'Dashboard',
              },
              {
                key: '2',
                icon: <UserOutlined />,
                label: 'Users',
              },
            ]}
          />
        </Sider>
        <Layout>
          <Header style={{ background: colorBgContainer, paddingInline: 48 }}>
            <h2 style={{ margin: 0 }}>SMART QHSE Platform</h2>
          </Header>
          <Content
            style={{
              margin: '24px 16px',
              padding: 24,
              background: colorBgContainer,
              borderRadius: borderRadiusLG,
            }}
          >
            <Routes>
              <Route path="/" element={<h1>Welcome to SMART QHSE Platform</h1>} />
            </Routes>
          </Content>
          <Footer style={{ textAlign: 'center' }}>
            SMART QHSE Platform ©2024
          </Footer>
        </Layout>
      </Layout>
    </Router>
  )
}

export default App

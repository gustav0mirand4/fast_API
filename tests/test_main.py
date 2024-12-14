
from fast_API.main import app
from http import HTTPStatus

def test_read_root(client):

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post('/users/', #Userschema
                json={
                    'username':'testusername',
                    'password':'password',
                    'email':'test@test.com.br'
                    }
                )

    # Voltou o status code correto
    assert response.status_code == HTTPStatus.CREATED
    # Validar o UserPublic

    assert response.json() == {
    
                    'username':'testusername',
                    'email':'test@test.com.br',
                    'id': 1               
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'users':
       [
        {
            'username':'testusername',
            'email':'test@test.com.br',
            'id': 1,               
            
      }
     ]
    }
    

def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password':'123',
            'username':'testusername02',
            'email':'test@test.com.br',
            'id': 1,
        }
    )

    assert response.json() == {
            'username':'testusername02',
            'email':'test@test.com.br',
            'id': 1,
        }
    

def test_delete_user(client):
    response = client.delete('users/1')

    assert response.json() == {"message": "User Deleted"}

    

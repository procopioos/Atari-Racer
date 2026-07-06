import pytest
import pygame

@pytest.fixture(scope="session", autouse=True)
def pygame_initialize():
    pygame.init()
    # some draw helpers need an active display
    pygame.display.set_mode((800, 600))
    yield
    pygame.quit()

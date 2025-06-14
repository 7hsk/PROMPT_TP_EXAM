#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module de gestion des permissions utilisateur.

Ce module fournit des fonctionnalités pour récupérer et gérer les permissions
des utilisateurs dans différents contextes système.
"""

from typing import Dict, List, Optional, Union
from dataclasses import dataclass
from enum import Enum
import logging
from datetime import datetime

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PermissionLevel(Enum):
    """Niveaux de permission disponibles dans le système."""
    NONE = 0
    READ = 1
    WRITE = 2
    ADMIN = 3

@dataclass
class SystemContext:
    """
    Contexte système pour la vérification des permissions.
    
    Attributes:
        system_id: Identifiant unique du système
        environment: Environnement (dev, prod, etc.)
        timestamp: Moment de la vérification
    """
    system_id: str
    environment: str
    timestamp: datetime = datetime.now()

def get_user_permissions(
    user_id: Union[int, str],
    system_context: SystemContext
) -> Dict[str, List[PermissionLevel]]:
    """
    Récupère les permissions d'un utilisateur dans un contexte système donné.
    
    Cette fonction vérifie les permissions d'un utilisateur en fonction de son
    identifiant et du contexte système spécifié. Elle retourne un dictionnaire
    des permissions par ressource.
    
    Args:
        user_id: Identifiant unique de l'utilisateur (entier ou chaîne)
        system_context: Contexte système contenant les informations de
            l'environnement et du système
    
    Returns:
        Dict[str, List[PermissionLevel]]: Dictionnaire des permissions par
            ressource. Les clés sont les identifiants des ressources et les
            valeurs sont les listes de niveaux de permission.
    
    Raises:
        ValueError: Si l'user_id est invalide ou si le contexte système
            est mal configuré
        PermissionError: Si l'utilisateur n'a pas les droits pour accéder
            aux informations de permission
    
    Examples:
        >>> context = SystemContext("sys_123", "production")
        >>> permissions = get_user_permissions(42, context)
        >>> print(permissions)
        {
            'resource_1': [PermissionLevel.READ, PermissionLevel.WRITE],
            'resource_2': [PermissionLevel.READ]
        }
        
        >>> # Exemple avec un utilisateur admin
        >>> admin_permissions = get_user_permissions("admin_1", context)
        >>> print(admin_permissions)
        {
            'resource_1': [PermissionLevel.ADMIN],
            'resource_2': [PermissionLevel.ADMIN],
            'resource_3': [PermissionLevel.ADMIN]
        }
    """
    # Validation des entrées
    if not user_id:
        raise ValueError("L'identifiant utilisateur ne peut pas être vide")
    
    if not system_context or not system_context.system_id:
        raise ValueError("Le contexte système est invalide")
    
    # Simulation de récupération des permissions
    # Dans un cas réel, cela impliquerait une requête à une base de données
    # ou un service d'authentification
    try:
        # Exemple de permissions simulées
        if str(user_id).startswith("admin"):
            return {
                "resource_1": [PermissionLevel.ADMIN],
                "resource_2": [PermissionLevel.ADMIN],
                "resource_3": [PermissionLevel.ADMIN]
            }
        else:
            return {
                "resource_1": [PermissionLevel.READ, PermissionLevel.WRITE],
                "resource_2": [PermissionLevel.READ]
            }
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des permissions: {e}")
        raise PermissionError("Impossible de récupérer les permissions")

def main() -> None:
    """Fonction principale avec exemples d'utilisation."""
    # Création d'un contexte système
    context = SystemContext(
        system_id="sys_123",
        environment="production"
    )
    
    # Exemple 1: Utilisateur normal
    try:
        permissions = get_user_permissions(42, context)
        print("\nPermissions utilisateur normal:")
        print(permissions)
    except (ValueError, PermissionError) as e:
        logger.error(f"Erreur: {e}")
    
    # Exemple 2: Utilisateur admin
    try:
        admin_permissions = get_user_permissions("admin_1", context)
        print("\nPermissions utilisateur admin:")
        print(admin_permissions)
    except (ValueError, PermissionError) as e:
        logger.error(f"Erreur: {e}")
    
    # Exemple 3: Cas d'erreur - ID invalide
    try:
        get_user_permissions("", context)
    except ValueError as e:
        logger.error(f"Erreur attendue: {e}")

if __name__ == "__main__":
    main() 
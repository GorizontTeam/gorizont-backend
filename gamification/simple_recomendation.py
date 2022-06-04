# from __future__ import print_function
import django
django.setup()
import locale
import sys

from accounts.models import User

from gamification.models import UserAchievement

sys.path.append("src/")
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def jaccard_index(set1,set2):
  set1    = set(set1)
  set2    = set(set2)
  intrsct = float(len(set1.intersection(set2)))
  union   = float(len(set1.union(set2)))
  jaccard_index = intrsct/union
  return round(jaccard_index,3)

#Считает топ 15 схожих пользователей для авторизованного пользователя
def get_top_N_similar(username, preferences, N):
    user_preference = preferences.filter(user__username=username)
    if user_preference:
        # similar = [(jaccard_index(user_preference, preference), other_user) for other_user, preference in
        #            preferences.iteritems() if other_user != username]
        similar = []
        for preference in preferences:
            if preference.user.username != username:
                # print(user_preference)
                # print(type(user_preference))
                # print(preference)
                # print(type(preference))
                # print(preference.user)
                # print(type(preference.user))
                current_iteration_user_preference = preferences.filter(user=preference.user)
                similar.append(
                    (jaccard_index(user_preference, current_iteration_user_preference), preference.user),
                )
        print(similar)
        similar.sort(reverse=True)
        return similar[:N]

#Считает количество пользователей, которые получили выбранное достижение
def occurs_in(post_id, preferences, users):
    count = 0
    for user in users:
        preference = preferences.filter(user=user)
        if post_id in preference:
            count += 1
    return count

def get_achievements_from_user_achievements(preferences):
    return preferences.value_list('achievement', flat=True)


# uncomment to make give_recommendations work!
def give_achievement_recommendations(username):
    N = 15  # количество пользователей в топе
    preferences = UserAchievement.objects.all()
    preference = preferences.filter(user__username=username)  # достигнутые достижения для выбранного(авторизованного) пользователя
    top_similar = get_top_N_similar(username, preferences, N)  # 15 пользователей с наибольшим сходством Жаккарда. На выходе получаем список пар сходство-пользователь
    similar_users = [user for snimilarity, user in top_similar]  # 15 пользователей с наибольшим сходством Жаккарда. На выходе получаем список пользователей(только пользователей)
    rank = {} # словарь коэффициентов сходства по достижениям
    for similarity, other_user in top_similar: # по схожести и другим пользователям из списка 15 топов проходимся
        other_preferences = preferences.filter(user=other_user) # список достигнутых достижений выбранного пользователя из списка 15 топов
        current_user_achievement = get_achievements_from_user_achievements(preference)
        other_user_achievements = get_achievements_from_user_achievements(other_preferences)
        for post_id in other_user_achievements: # для id достижения пользователя из other_preferences
            if post_id not in current_user_achievement: # проверяем достигнуто ли достижение авторизованным пользователем
                rank.setdefault(post_id, 0) # создаём пустую запись для достижения в ранк, если она не была создана раньше
                rank[post_id] += similarity # прибавляем коэффициент сходства для достижения
    recommendations = [(similarity / occurs_in(post_id, preferences, similar_users), post_id) for post_id, similarity in rank.iteritems()] #получаем список достижение-коэффициент насколько подходит для всех достижений
    recommendations.sort(reverse=True) # Сортируем полученный список
    recommendation_topM = recommendations[0] # Достаём одно необходимое рекомендованное достижение
    return (recommendation_topM)

if __name__ == "__main__":
    user = User.objects.get(id=8)
    recommedations = give_achievement_recommendations(username=user.username)
    print(recommedations)

# from gamification.simple_recomendation import give_achievement_recommendations
# from accounts.models import User
# user = User.objects.get(id=8)
# give_achievement_recommendations(username=user.username)
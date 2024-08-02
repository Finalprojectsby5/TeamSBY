import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    # Load the dataset
    df = pd.read_csv('cleaned_credit_card.csv')

    # Map 0 to "Approved" and 1 to "Rejected"
    df['application_status'] = df['label'].apply(lambda x: 'Approved' if x == 0 else 'Rejected')

    st.title('Exploratory Data Analysis')

    st.write('### Dataset Overview')
    st.write(df.head())

    st.write('### Dataset Summary')
    st.write(df.describe())

    # Plot 1: Distribution of Credit Card Approval
    st.write('### Distribution of Credit Card Approval')
    fig, ax = plt.subplots(figsize=(8, 6))
    df['application_status'].value_counts().plot.pie(autopct='%1.1f%%', colors=plt.cm.viridis.colors, ax=ax)
    plt.ylabel('')
    plt.title('Distribution of Credit Card Approval')
    st.pyplot(fig)

    # Plot 2: Mean Annual Income by Credit Card Application Status
    st.write('### Mean Annual Income by Credit Card Application Status')
    income_by_label = df.groupby('application_status')['annual_income'].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=income_by_label.index, y=income_by_label.values, ax=ax, palette="viridis")
    plt.xlabel('Credit Card Application Status')
    plt.ylabel('Mean Annual Income')
    plt.title('Mean Annual Income by Credit Card Application Status')
    for p in ax.patches:
        value = '{:.0f}'.format(p.get_height())
        x = p.get_x() + p.get_width() / 2 - 0.15
        y = p.get_y() + p.get_height() + 0.01 * income_by_label.max()
        ax.annotate(value, (x, y), size=12)
    st.pyplot(fig)

    # Plot 3: Percentage of Rejected Credit Card Applications by Type of Income
    st.write('### Percentage of Rejected Credit Card Applications by Type of Income')
    grouped = df.groupby(['type_income', 'application_status'])['type_income'].count().unstack()
    grouped['Rejection Percentage'] = (grouped['Rejected'] / (grouped['Approved'] + grouped['Rejected'])) * 100
    grouped = grouped.sort_values('Rejection Percentage', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=grouped.index, y=grouped['Rejection Percentage'], ax=ax, palette="viridis")
    plt.xlabel('Type of Income')
    plt.ylabel('Percentage of Rejected Applications')
    plt.title('Percentage of Rejected Credit Card Applications by Type of Income')
    plt.xticks(rotation=45, ha='right')
    for p in ax.patches:
        percentage = '{:.1f}%'.format(p.get_height())
        x = p.get_x() + p.get_width() / 2
        y = p.get_y() + p.get_height()
        ax.annotate(percentage, (x, y), ha='center', va='bottom', size=12, color='black', weight='bold')
    st.pyplot(fig)

    # Plot 4: Percentage of Rejected Credit Card Applications by Housing Type
    st.write('### Percentage of Rejected Credit Card Applications by Housing Type')
    housing_counts = df.groupby(['housing_type', 'application_status'])['housing_type'].count().unstack()
    housing_rejection_percentage = (housing_counts['Rejected'] / housing_counts.sum(axis=1)) * 100
    housing_rejection_percentage = housing_rejection_percentage.sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=housing_rejection_percentage.index, y=housing_rejection_percentage.values, ax=ax, palette="viridis")
    plt.xlabel('Housing Type', fontsize=14)
    plt.ylabel('Percentage of Rejected Applications', fontsize=14)
    plt.title('Percentage of Rejected Credit Card Applications by Housing Type', fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    for p in ax.patches:
        value = '{:.1f}%'.format(p.get_height())
        x = p.get_x() + p.get_width() / 2
        y = p.get_y() + p.get_height()
        ax.annotate(value, (x, y), ha='center', va='bottom', size=12, color='black', weight='bold')
    st.pyplot(fig)

    # Plot 5: Percentage of Rejected Credit Card Applications by Type of Occupation
    st.write('### Percentage of Rejected Credit Card Applications by Type of Occupation')
    grouped = df.groupby(['type_occupation', 'application_status'])['type_occupation'].count().unstack()
    grouped['Rejection Percentage'] = (grouped['Rejected'] / (grouped['Approved'] + grouped['Rejected'])) * 100
    grouped = grouped.sort_values('Rejection Percentage', ascending=False)
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.barplot(x=grouped.index, y=grouped['Rejection Percentage'], ax=ax, palette="viridis")
    plt.xlabel('Type of Occupation', fontsize=14)
    plt.ylabel('Percentage of Rejected Applications', fontsize=14)
    plt.title('Percentage of Rejected Credit Card Applications by Type of Occupation', fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    for p in ax.patches:
        percentage = '{:.1f}%'.format(p.get_height())
        x = p.get_x() + p.get_width() / 2
        y = p.get_y() + p.get_height()
        ax.annotate(percentage, (x, y), ha='center', va='bottom', size=12, color='black', weight='bold')
    st.pyplot(fig)

    # Plot 6: Percentage of Rejected Credit Card Applications by Customer Age
    st.write('### Percentage of Rejected Credit Card Applications by Customer Age')
    bins = [20, 30, 40, 50, 60]
    labels = ['20-29', '30-39', '40-49', '50-59']
    df['age_group'] = pd.cut(df['customer_age_years'], bins=bins, labels=labels, right=False)
    grouped = df.groupby(['age_group', 'application_status'])['age_group'].count().unstack()
    grouped['Rejection Percentage'] = (grouped['Rejected'] / (grouped['Approved'] + grouped['Rejected'])) * 100
    grouped = grouped.sort_values('Rejection Percentage', ascending=False)
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.barplot(x=grouped.index, y=grouped['Rejection Percentage'], ax=ax, palette="viridis")
    plt.xlabel('Age Group', fontsize=14)
    plt.ylabel('Percentage of Rejected Applications', fontsize=14)
    plt.title('Impact of Age on Credit Card Application Rejections', fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    for p in ax.patches:
        percentage = '{:.1f}%'.format(p.get_height())
        x = p.get_x() + p.get_width() / 2
        y = p.get_y() + p.get_height()
        ax.annotate(percentage, (x, y), ha='center', va='bottom', size=12, color='black', weight='bold')
    st.pyplot(fig)

if __name__ == "__main__":
    run()
